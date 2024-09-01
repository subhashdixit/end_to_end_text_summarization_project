from text_summarizer.constants import *  # Import path constants
from text_summarizer.utils.common import read_yaml, create_directories  # Import utility functions
from text_summarizer.entity import (  # Import data classes for configuration
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
    ModelEvaluationConfig
)

class ConfigurationManager:
    """
    ConfigurationManager is responsible for managing the configuration of the project. 
    It reads configuration and parameter files, creates necessary directories, 
    and provides methods to get configuration for different components.
    """
    
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,  # Default path to the configuration YAML file
        params_filepath = PARAMS_FILE_PATH  # Default path to the parameters YAML file
    ):
        """
        Initializes the ConfigurationManager with configuration and parameters.
        
        Args:
            config_filepath (Path): Path to the configuration file.
            params_filepath (Path): Path to the parameters file.
        """
        self.config = read_yaml(config_filepath)  # Load configuration from YAML file
        self.params = read_yaml(params_filepath)  # Load parameters from YAML file

        create_directories([self.config.artifacts_root])  # Create root directory for artifacts

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Retrieves data ingestion configuration.

        Returns:
            DataIngestionConfig: Data ingestion configuration object.
        """
        config = self.config.data_ingestion  # Access data ingestion configuration section

        create_directories([config.root_dir])  # Create directory for data ingestion

        # Create and return DataIngestionConfig object
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config

    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Retrieves data validation configuration.

        Returns:
            DataValidationConfig: Data validation configuration object.
        """
        config = self.config.data_validation  # Access data validation configuration section

        create_directories([config.root_dir])  # Create directory for data validation

        # Create and return DataValidationConfig object
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )
        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        """
        Retrieves data transformation configuration.

        Returns:
            DataTransformationConfig: Data transformation configuration object.
        """
        config = self.config.data_transformation  # Access data transformation configuration section

        create_directories([config.root_dir])  # Create directory for data transformation

        # Create and return DataTransformationConfig object
        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name=config.tokenizer_name
        )
        return data_transformation_config

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        """
        Retrieves model training configuration.

        Returns:
            ModelTrainerConfig: Model training configuration object.
        """
        config = self.config.model_trainer  # Access model trainer configuration section
        params = self.params.TrainingArguments  # Access training parameters from params file

        create_directories([config.root_dir])  # Create directory for model training

        # Create and return ModelTrainerConfig object
        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_ckpt=config.model_ckpt,
            num_train_epochs=params.num_train_epochs,
            warmup_steps=params.warmup_steps,
            per_device_train_batch_size=params.per_device_train_batch_size,
            weight_decay=params.weight_decay,
            logging_steps=params.logging_steps,
            evaluation_strategy=params.evaluation_strategy,
            eval_steps=params.eval_steps,  # Fixed to use eval_steps instead of evaluation_strategy
            save_steps=params.save_steps,
            gradient_accumulation_steps=params.gradient_accumulation_steps
        )
        return model_trainer_config

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        """
        Retrieves model evaluation configuration.

        Returns:
            ModelEvaluationConfig: Model evaluation configuration object.
        """
        config = self.config.model_evaluation  # Access model evaluation configuration section

        create_directories([config.root_dir])  # Create directory for model evaluation

        # Create and return ModelEvaluationConfig object
        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_path=config.model_path,
            tokenizer_path=config.tokenizer_path,
            metric_file_name=config.metric_file_name
        )
        return model_evaluation_config
