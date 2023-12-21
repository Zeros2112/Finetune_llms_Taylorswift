# Import custom utility functions and modules
from utilities import *

# Define a function for building a configuration set
def build_config(existing_config=None):
    # Initialize a list to store configuration instances
    configs = [
        # Using config library to load configurations from environment variables
        config.config_from_env(prefix="LLAMA", separator="_", lowercase_keys=True),
    ]

    # Check if an existing configuration is provided
    if existing_config:
        # If it's a dictionary, convert it to a configuration instance
        if isinstance(existing_config, dict):
            configs.append(config.config_from_dict(existing_config))
        # If it's already a configuration instance, use it directly
        else:
            configs.append(existing_config)

    # Get a list of configuration paths
    config_paths = get_config_paths()

    # Iterate over the reversed list of configuration paths
    for path in reversed(config_paths):
        # Print a message indicating that a configuration is being loaded from a specific path
        print("Loading builtin config from " + path)
        
        # Load configurations from a YAML file and append to the list
        configs.append(config.config_from_yaml(path, read_from_file=True))

    # Return a ConfigurationSet instance containing all configurations
    return config.ConfigurationSet(*configs)
