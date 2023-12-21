# Import custom utility functions and modules
from utilities import *

# Define a function for tokenizing and splitting training data
def tokenize_and_split_data(training_config, tokenizer):
    # Initialize configuration and logging
    initialized_config = initialize_config_and_logging(training_config)

    # Extract dataset path and use_hf flag from the configuration
    dataset_path = initialized_config["datasets"]["path"]
    use_hf = initialized_config["datasets"]["use_hf"]

    # Print information about the tokenization process
    print("tokenize", use_hf, dataset_path)

    # Load dataset using the Hugging Face datasets library if use_hf is True
    if use_hf:
        dataset = datasets.load_dataset(dataset_path)
    # Otherwise, load dataset using a custom function (load_dataset) with the provided tokenizer
    else:
        dataset = load_dataset(dataset_path, tokenizer)

    # Extract training and testing datasets from the loaded dataset
    train_dataset = dataset["train"]
    test_dataset = dataset["test"]

    # Return the tokenized training and testing datasets
    return train_dataset, test_dataset

