from text_summarizer.config.configuration import ConfigurationManager  # Importing ConfigurationManager for managing configuration settings
from text_summarizer.components.data_transformation import DataTransformation  # Importing DataTransformation for transforming data
from text_summarizer.logging import logger  # Importing logger for logging (not used in this snippet)


class DataTransformationTrainingPipeline:
    def __init__(self):
        """
        Initializes the DataTransformationTrainingPipeline class.
        """
        pass

    def main(self):
        """
        Main method for executing the data transformation pipeline.
        1. Loads configuration settings.
        2. Initializes the DataTransformation with the loaded configuration.
        3. Executes the data transformation process.
        """
        # Load configuration settings using ConfigurationManager
        config = ConfigurationManager()
        
        # Retrieve data transformation configuration
        data_transformation_config = config.get_data_transformation_config()
        
        # Initialize DataTransformation with the retrieved configuration
        data_transformation = DataTransformation(config=data_transformation_config)
        
        # Execute the data transformation process
        data_transformation.convert()
