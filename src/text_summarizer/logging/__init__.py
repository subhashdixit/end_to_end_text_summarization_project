import os  # Import the os module for interacting with the operating system, such as creating directories and joining paths.
import sys  # Import the sys module to access system-specific parameters and functions, such as standard output.
import logging  # Import the logging module for generating log messages.

# Define the format for log messages. Includes timestamp, log level, module name, and message.
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Define the directory where log files will be stored.
log_dir = "logs"

# Define the file path for the log file, combining the log directory and file name.
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create the log directory if it does not already exist.
os.makedirs(log_dir, exist_ok=True)

# Configure the logging settings.
logging.basicConfig(
    level=logging.INFO,  # Set the logging level to INFO, which means all messages at this level and higher will be captured.
    format=logging_str,  # Set the format for log messages using the previously defined format string.

    handlers=[
        logging.FileHandler(log_filepath),  # Output log messages to a file specified by log_filepath.
        logging.StreamHandler(sys.stdout)    # Output log messages to the standard output (console).
    ]
)

# Create a logger instance with the name "textSummarizerLogger".
logger = logging.getLogger("textSummarizerLogger")
