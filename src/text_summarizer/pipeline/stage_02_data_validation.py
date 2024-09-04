from text_summarizer.config.configuration import ConfigurationManager  # Importing the ConfigurationManager class for managing configuration
from text_summarizer.components.data_validation import DataValidation  # Importing the DataValidation class for data validation tasks
from text_summarizer.logging import logger  # Importing the logger for logging purposes

class DataValidationTrainingPipeline:
    def __init__(self):
        """
        Initialize the DataValidationTrainingPipeline class.
        """
        pass

    def main(self):
        """
        Main method to execute the data validation pipeline.
        """
        # Create an instance of ConfigurationManager to access configuration settings
        config = ConfigurationManager()

        # Retrieve the data validation configuration
        data_validation_config = config.get_data_validation_config()

        # Create an instance of DataValidation with the obtained configuration
        data_validation = DataValidation(config=data_validation_config)

        # Perform data validation to check if all required files are present
        data_validation.validate_all_files_exist()
