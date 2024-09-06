from text_summarizer.config.configuration import ConfigurationManager  # Import ConfigurationManager for fetching configuration
from text_summarizer.components.model_evaluation import ModelEvaluation  # Import ModelEvaluation for evaluating the model
from text_summarizer.logging import logger  # Import logger for logging messages


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        """
        Initializes the ModelEvaluationTrainingPipeline class.
        """
        pass

    def main(self):
        """
        Main method to execute the model evaluation pipeline.
        - Fetches the configuration settings.
        - Initializes the ModelEvaluation class with the configuration.
        - Calls the evaluate method to perform model evaluation.
        """
        # Fetch configuration settings
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        
        # Initialize ModelEvaluation with the fetched configuration
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        
        # Perform model evaluation
        model_evaluation.evaluate()
