from text_summarizer.config.configuration import ConfigurationManager  # Import ConfigurationManager for loading config
from text_summarizer.components.model_trainer import ModelTrainer  # Import ModelTrainer class for model training
from text_summarizer.logging import logger  # Import logger for logging purposes


class ModelTrainerTrainingPipeline:
    def __init__(self):
        """
        Initializes the ModelTrainerTrainingPipeline class. 
        No specific setup is required during initialization.
        """
        pass

    def main(self):
        """
        Executes the main pipeline for model training.
        1. Loads configuration settings using ConfigurationManager.
        2. Initializes the ModelTrainer with the loaded configuration.
        3. Starts the training process.
        """
        # Load configuration settings for model training
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        
        # Initialize the ModelTrainer with the loaded configuration
        model_trainer = ModelTrainer(config=model_trainer_config)
        
        # Execute the training process
        model_trainer.train()
