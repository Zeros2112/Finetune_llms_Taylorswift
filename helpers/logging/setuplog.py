# Import custom utility functions and modules
from utilities import *

# Define a function for setting up logging based on provided arguments
def setup_logging(arguments):
    # Define the logging format with timestamp, log level, logger name, and log message
    logging_format = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"

    # Configure logging based on verbosity level in the arguments
    if arguments["verbose"]:
        logging.basicConfig(level=logging.DEBUG, format=logging_format)
    elif arguments["verbose_info"]:
        logging.basicConfig(level=logging.INFO, format=logging_format)
    else:
        logging.basicConfig(level=logging.WARNING, format=logging_format)

    # Get the root logger
    root_logger = logging.getLogger()

    # Set the logging level for the root logger based on verbosity level in the arguments
    if arguments["verbose"]:
        root_logger.setLevel(logging.DEBUG)
    elif arguments["verbose_info"]:
        root_logger.setLevel(logging.INFO)
    else:
        root_logger.setLevel(logging.WARNING)

    # Set specific log levels for certain loggers to suppress unnecessary log messages
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("filelock").setLevel(logging.WARNING)
    logging.getLogger("smart_open").setLevel(logging.WARNING)
    logging.getLogger("botocore").setLevel(logging.WARNING)
