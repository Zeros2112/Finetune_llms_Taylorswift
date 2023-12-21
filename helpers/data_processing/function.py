# Import custom utility functions and modules
from utilities import *

# Define a function to generate a tokenize function based on configuration parameters
def get_tokenize_function(tokenizer, _max_length):

    # Define a tokenize function that takes examples and tokenizes the text
    def tokenize_function(examples):
        # Use the provided maximum length or the one specified in the configuration
        max_length = _max_length

        # Set the pad token of the tokenizer to the end-of-sequence token
        tokenizer.pad_token = tokenizer.eos_token

        # Determine the text to tokenize based on available keys in the examples
        if "question" in examples and "answer" in examples:
            text = examples["question"][0] + examples["answer"][0]
        elif "input" in examples and "output" in examples:
            text = examples["input"][0] + examples["output"][0]
        else:
            text = examples["text"][0]

        # Run the tokenizer on the text, returning tensors in a NumPy array
        tokenized_inputs = tokenizer(
            text,

            # Specify the return format for tensors (options: "np", "pt", "tf")
            return_tensors="np",

            # Specify the padding type (options: True, False, "max_length")
            padding=True,
        )

        # Calculate the maximum length based on the input_ids shape
        max_length = min(
            tokenized_inputs["input_ids"].shape[1],
            max_length
        )

        # Check if truncation is needed and truncate if necessary
        if tokenized_inputs["input_ids"].shape[1] > max_length:
            logger.warn(
                f"Truncating input from {tokenized_inputs['input_ids'].shape[1]} to {max_length}"
            )

        # Set the truncation side to "left"
        tokenizer.truncation_side = "left"

        # Re-run the tokenizer with truncation enabled
        tokenized_inputs = tokenizer(
            text,
            return_tensors="np",
            truncation=True,
        )

        # Assign the input_ids as labels for the tokenized inputs
        tokenized_inputs["labels"] = tokenized_inputs["input_ids"]

        # Return the tokenized inputs
        return tokenized_inputs

    # Return the generated tokenize function
    return tokenize_function

