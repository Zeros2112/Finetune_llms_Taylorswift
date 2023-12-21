# Import custom utility functions and modules
from utilities import *

# Define a function for initializing configuration and logging
def initialize_config_and_logging(existing_config=None):
    # Declare global variables for configuration
    global global_config

    # Build configuration using the provided or default configuration
    global_config = build_config(existing_config)

    # Set up logging based on the configuration
    setup_logging(global_config)

    # Log the configuration details at DEBUG level
    logger.debug("Config: " + str(yaml.dump(global_config.as_dict())))

    # Return the initialized global configuration
    return global_config
