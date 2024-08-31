import os  # Provides functions to interact with the operating system, such as creating directories and handling paths.
from box.exceptions import BoxValueError  # Exception class from the `box` library for handling specific errors related to `ConfigBox`.
import yaml  # PyYAML library for reading and writing YAML files.
from text_summarizer.logging import logger  # Import the logger object for logging messages, configured in the `text_summarizer` package.
from ensure import ensure_annotations  # Decorator from `ensure` for type annotations and validation.
from box import ConfigBox  # `ConfigBox` class from the `box` library for handling nested data structures.
from pathlib import Path  # Provides object-oriented file system paths.
from typing import Any  # Import `Any` for type hints in function signatures.


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its content as a ConfigBox.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        e: Any other exception raised during file reading.

    Returns:
        ConfigBox: The content of the YAML file wrapped in a ConfigBox for easy access.
    """
    try:
        with open(path_to_yaml) as yaml_file:  # Open the YAML file for reading.
            content = yaml.safe_load(yaml_file)  # Load the content of the YAML file.
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")  # Log a success message.
            return ConfigBox(content)  # Return the content wrapped in a ConfigBox.
    except BoxValueError:  # Handle specific errors related to `ConfigBox`.
        raise ValueError("YAML file is empty")  # Raise a ValueError if the file is empty.
    except Exception as e:  # Handle any other exceptions.
        raise e  # Re-raise the exception for handling elsewhere.


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of directories.

    Args:
        path_to_directories (list): A list of paths for directories to be created.
        verbose (bool, optional): If True, log messages will be created for each directory. Defaults to True.
    """
    for path in path_to_directories:  # Iterate over each path in the list.
        os.makedirs(path, exist_ok=True)  # Create the directory if it does not exist.
        if verbose:  # Check if verbose logging is enabled.
            logger.info(f"Created directory at: {path}")  # Log a message indicating the directory was created.


@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in kilobytes (KB).

    Args:
        path (Path): The path to the file whose size is to be determined.

    Returns:
        str: The size of the file in KB, formatted as a string.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)  # Calculate the size of the file in KB and round it.
    return f"~ {size_in_kb} KB"  # Return the size as a string formatted to include the approximate size in KB.
