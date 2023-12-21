# Import custom utility functions and modules
from utilities import *

# Define a custom Trainer class that extends transformers.Trainer
class Trainer(transformers.Trainer):
    def __init__(
        self,
        model,
        model_flops,
        total_steps,
        args=None,
        data_collator=None,
        train_dataset=None,
        eval_dataset=None,
        tokenizer=None,
        model_init=None,
        compute_metrics=None,
        callbacks=None,
        optimizers=(None, None),
    ):
        # Call the constructor of the parent class (transformers.Trainer)
        super(Trainer, self).__init__(
            model,
            args,
            data_collator,
            train_dataset,
            eval_dataset,
            tokenizer,
            model_init,
            compute_metrics,
            callbacks,
            optimizers,
        )

        # Initialize custom attributes for tracking total steps, model flops, and starting step
        self.total_steps = total_steps
        self.model_flops = model_flops
        self.start_step = 0

    def training_step(self, model, inputs):
        # Custom training step to handle empty input_ids
        if inputs["input_ids"].numel() == 0:
            # Log information about empty inputs and return a tensor with value 0
            print("Inputs: ", inputs)
            print("Inputs - input_ids", inputs["input_ids"])
            print("numel", inputs["input_ids"].numel())
            return torch.tensor(0)
        else:
            # Set the model in training mode
            model.train()

            # Prepare inputs for training
            inputs = self._prepare_inputs(inputs)

            # Calculate the loss using the compute_loss method
            with self.compute_loss_context_manager():
                loss = self.compute_loss(model, inputs)

            # Perform additional operations for multi-GPU parallel training
            if self.args.n_gpu > 1:
                loss = loss.mean()  # mean() to average on multi-GPU parallel training

            # Scale the loss and perform backward pass
            if self.do_grad_scaling:
                self.scaler.scale(loss).backward()
            else:
                self.accelerator.backward(loss)

            # Return the detached loss normalized by gradient accumulation steps
            return loss.detach() / self.args.gradient_accumulation_steps

    def log(self, logs):
        """
        Log `logs` on the various objects watching training.
        Subclass and override this method to inject custom behavior.
        Args:
            logs (`Dict[str, float]`):
                The values to log.
        """
        # If an epoch is available, round and add it to the logs
        if self.state.epoch is not None:
            logs["epoch"] = round(self.state.epoch, 2)

        # Update log timing, history, and call the callback handler for logging
        self.update_log_timing(logs)
        output = {**logs, **{"step": self.state.global_step}}
        self.update_history(output)

        # Log step information
        logger.debug("Step (" + str(self.state.global_step) + ") Logs: " + str(logs))
        self.control = self.callback_handler.on_log(
            self.args, self.state, self.control, logs
        )

    def update_log_timing(self, logs):
        # Update log timing information based on the current training step
        if len(self.state.log_history) == 0:
            self.start_time = time.time()
            logs["iter_time"] = 0.0
            logs["flops"] = 0.0
            logs["remaining_time"] = 0.0
            self.start_step = self.state.global_step
        elif self.state.global_step > self.start_step:
            logs["iter_time"] = (time.time() - self.start_time) / (
                self.state.global_step - self.start_step
            )
            logs["flops"] = self.model_flops / logs["iter_time"]
            logs["remaining_time"] = (self.total_steps - self.state.global_step) * logs[
                "iter_time"
            ]

    def update_history(self, output):
        # Update training history, applying smoothing to the loss if available
        if "eval_loss" in output:
            return
        if len(self.state.log_history) > 0:
            smoothing_window = 100
            p = 1.0 / smoothing_window
            if "loss" in output:
                output["loss"] = output["loss"] * p + self.state.log_history[-1][
                    "loss"
                ] * (1.0 - p)
        self.state.log_history.append(output)
