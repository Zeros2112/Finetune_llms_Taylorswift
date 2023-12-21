# Import custom utility functions and modules
from utilities import *

# Define a function to load a language model onto the right device and load its tokenizer
def load_model(training_config, load_base_model=False):
    # Initialize the model_load_path variable
    model_load_path = ""
    model_load_path = training_config["model"]["pretrained_name"]

    # Log a debug message indicating the default model is being loaded
    logger.debug(f"Loading default model: {model_load_path}")

    # Load the language model from the specified pretrained path
    model = AutoModelForCausalLM.from_pretrained(model_load_path)

    # Load the tokenizer corresponding to the loaded model
    tokenizer = AutoTokenizer.from_pretrained(model_load_path)

    # Log a debug message indicating that the model is being copied to the appropriate device
    logger.debug("Copying model to device")

    # Check the number of available GPU devices
    device_count = torch.cuda.device_count()

    # Select the appropriate device (GPU if available, otherwise CPU)
    if device_count > 0:
        logger.debug("Select GPU device")
        device = torch.device("cuda")
    else:
        logger.debug("Select CPU device")
        device = torch.device("cpu")

    # Move the loaded model to the selected device
    model.to(device)

    # Log a debug message indicating that the model copying process has finished
    logger.debug("Copying finished...")

    # Determine the model name based on the configuration or use the pretrained_name
    if "model_name" not in training_config:
        model_name = model_load_path
    else:
        model_name = training_config["model_name"]

    # Return the loaded model, tokenizer, selected device, and model name
    return model, tokenizer, device, model_name
