import os
import urllib.request as request
import zipfile
from text_summarizer.logging import logger  # Import custom logger for logging messages
from text_summarizer.utils.common import get_size  # Import utility function for file size
from pathlib import Path
from text_summarizer.entity import DataIngestionConfig  # Import DataIngestionConfig class

class DataIngestion:
    """
    DataIngestion is responsible for downloading and extracting data files. 
    It handles the downloading of files from a specified URL and extracting
    ZIP archives into a designated directory.
    """

    def __init__(self, config: DataIngestionConfig):
        """
        Initializes the DataIngestion instance with configuration settings.

        Args:
            config (DataIngestionConfig): Configuration settings for data ingestion.
        """
        self.config = config  # Store the configuration settings

    def download_file(self):
        """
        Downloads the file from the specified URL if it does not already exist.

        Checks if the file exists locally; if not, it downloads the file
        from the source URL and logs the download information. If the file
        already exists, logs its size.
        """
        if not os.path.exists(self.config.local_data_file):
            # Download the file from the source URL
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! with following info: \n{headers}")
        else:
            # Log that the file already exists and its size
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        Extracts the ZIP file into the specified directory.

        Unzips the downloaded file into the directory specified in the
        configuration. Creates the directory if it does not exist.

        Function returns None.
        """
        unzip_path = self.config.unzip_dir  # Directory to extract files into
        os.makedirs(unzip_path, exist_ok=True)  # Create directory if it does not exist
        # Open and extract the ZIP file
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)  # Extract all contents of the ZIP file
