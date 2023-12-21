# Import custom utility functions and modules
from utilities import *

# Define a function for loading and tokenizing a dataset
def load_dataset(dataset_path, tokenizer):
    # Set a seed for reproducibility
    random.seed(42)

    # Load the dataset from JSON files using Hugging Face datasets library
    finetuning_dataset_loaded = datasets.load_dataset("json", data_files=dataset_path, split="train")

    # Set the pad token of the tokenizer to the end-of-sequence token
    tokenizer.pad_token = tokenizer.eos_token

    # Extract the maximum length of the sequences from the model configuration
    max_length = training_config["model"]["max_length"]

    # Tokenize the loaded dataset using a custom tokenize function
    tokenized_dataset = finetuning_dataset_loaded.map(
        get_tokenize_function(tokenizer, max_length),  # returns tokenize_function
        batched=True,
        batch_size=1,
        drop_last_batch=True
    )

    # Convert the tokenized dataset to the torch format
    tokenized_dataset = tokenized_dataset.with_format("torch")

    # Split the tokenized dataset into training and testing sets
    split_dataset = tokenized_dataset.train_test_split(test_size=0.1, shuffle=True, seed=123)

    # Return the split dataset
    return split_dataset

