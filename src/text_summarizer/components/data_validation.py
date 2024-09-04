import os
from text_summarizer.logging import logger  # Importing a logger for logging purposes
from text_summarizer.entity import DataValidationConfig  # Importing configuration class for data validation

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        """
        Initialize the DataValidation class with the provided configuration.
        
        :param config: DataValidationConfig object containing validation settings.
        """
        self.config = config

    def validate_all_files_exist(self) -> bool:
        """
        Validate if all required files exist in the specified directory.

        :return: True if all required files are present, False otherwise.
        """
        try:
            # Get the list of files in the target directory
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

            # Initialize validation status
            validation_status = True

            # Check each required file against the files in the directory
            for file in self.config.ALL_REQUIRED_FILES:
                if file not in all_files:
                    # If any required file is missing, update the status and log the issue
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                    break  # Exit the loop early since a missing file was found

            # Update the status file with the final validation result
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            # Log any exceptions raised during the validation process
            logger.error(f"An error occurred during file validation: {e}")
            raise e
