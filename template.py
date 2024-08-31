import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "text_summarizer"
list_of_files = [
    ".github/workflows/.gitkeep",  # Ensures .github/workflows directory is tracked by Git; used for GitHub Actions workflows.
    f"src/{project_name}/__init__.py",  # Initializes the src/{project_name} directory as a Python package for importing modules.
    f"src/{project_name}/components/__init__.py",  # Initializes the components directory as a Python package; used for organizing project components.
    f"src/{project_name}/utils/__init__.py",  # Initializes the utils directory as a Python package; typically contains utility functions.
    f"src/{project_name}/utils/common.py",  # Contains utility functions commonly used throughout the project.
    f"src/{project_name}/logging/__init__.py",  # Initializes the logging directory as a Python package; used for logging configuration and management.
    f"src/{project_name}/config/__init__.py",  # Initializes the config directory as a Python package; used for configuration settings.
    f"src/{project_name}/config/configuration.py",  # Contains configuration settings for different environments (e.g., development, production).
    f"src/{project_name}/pipeline/__init__.py",  # Initializes the pipeline directory as a Python package; contains data processing and model training pipelines.
    f"src/{project_name}/entity/__init__.py",  # Initializes the entity directory as a Python package; used for managing data entities or structures.
    f"src/{project_name}/constants/__init__.py",  # Initializes the constants directory as a Python package; used for storing constants and configuration values.
    "config/config.yaml",  # YAML configuration file used to specify settings and parameters in a human-readable format.
    "params.yaml",  # YAML file for specifying parameters for different components, such as machine learning models.
    "app.py",  # Main application script; entry point for running the project or starting the main functionality.
    "main.py",  # Main script to execute the project; typically used to initialize and run key functions or orchestrate the application.
    "Dockerfile",  # Dockerfile containing instructions to build a Docker image for containerizing the application.
    "requirements.txt",  # Lists Python package dependencies for the project; used by pip to install required packages.
    "setup.py",  # Setup script for packaging and distributing the project as a Python package; includes metadata and dependencies.
    "research/trials.ipynb",  # Jupyter Notebook used for research, experimentation, and exploratory analysis.
]



# Loop through each file path in the list_of_files
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert the file path string to a Path object for easier manipulation
    filedir, filename = os.path.split(filepath)  # Split the path into directory and file name components

    if filedir != "":  # Check if the directory part of the path is not empty
        os.makedirs(filedir, exist_ok=True)  # Create the directory if it does not exist; 'exist_ok=True' avoids raising an error if the directory already exists
        logging.info(f"Creating directory: {filedir} for the file {filename}")  # Log the creation of the directory

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  # Check if the file does not exist or if it is empty
        with open(filepath, 'w') as f:  # Open the file in write mode (this will create an empty file if it doesn't exist)
            pass  # No content is written to the file; it's just created
        logging.info(f"Creating empty file: {filepath}")  # Log the creation of the empty file

    else:  # If the file exists and is not empty
        logging.info(f"{filename} already exists")  # Log that the file already exists
