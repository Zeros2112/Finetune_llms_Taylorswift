# Import custom utility functions and modules
from utilities import *

# Define a function to retrieve the global configuration
def get_config():
    # Ensure that the global configuration variable is not None
    global global_config
    assert global_config is not None

    # Return the global configuration
    return global_config

# Define a function to get configuration paths
def get_config_paths():
    # Initialize an empty list to store configuration paths
    paths = []

    # Define the name and base directory for the configuration file
    config_name = "llama_config"
    config_base = "configs"

    # Construct paths for different configuration files and check if they exist
    base_config_path = os.path.join(config_base, config_name + ".yaml")
    if os.path.exists(base_config_path):
        paths.append(base_config_path)

    local_config_path = os.path.join(config_base, config_name + "_local.yaml")
    if os.path.exists(local_config_path):
        paths.append(local_config_path)

    home = os.path.expanduser("~")
    home_config_path = os.path.join(home, "." + config_name + ".yaml")
    if os.path.exists(home_config_path):
        paths.append(home_config_path)

    # Return the list of configuration paths
    return paths
