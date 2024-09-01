from text_summarizer.config.configuration import ConfigurationManager  # Import ConfigurationManager for config management
from text_summarizer.components.data_ingestion import DataIngestion  # Import DataIngestion for handling data tasks
from text_summarizer.logging import logger  # Import custom logger for logging messages

class DataIngestionTrainingPipeline:
    """
    DataIngestionTrainingPipeline orchestrates the data ingestion process.
    It manages the configuration and coordinates the data download and
    extraction steps.
    """

    def __init__(self):
        """
        Initializes the DataIngestionTrainingPipeline instance.
        """
        pass  # No initialization required for now

    def main(self):
        """
        Executes the main pipeline for data ingestion.
        
        This method:
        1. Retrieves configuration settings for data ingestion.
        2. Initializes the DataIngestion class with the configuration.
        3. Downloads the data file if not already present.
        4. Extracts the ZIP file contents to the specified directory.
        """
        # Load the configuration settings
        config = ConfigurationManager()
        
        # Get data ingestion configuration from the config manager
        data_ingestion_config = config.get_data_ingestion_config()
        
        # Initialize DataIngestion with the retrieved configuration
        data_ingestion = DataIngestion(config=data_ingestion_config)
        
        # Download the data file
        data_ingestion.download_file()
        
        # Extract the ZIP file contents
        data_ingestion.extract_zip_file()
