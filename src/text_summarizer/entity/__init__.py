from dataclasses import dataclass
from pathlib import Path

# DataIngestionConfig holds configuration related to data ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path  # Directory where ingested data will be stored
    source_URL: str  # URL to download the source data
    local_data_file: Path  # Path to save the downloaded data file
    unzip_dir: Path  # Directory where the downloaded data will be extracted

# DataValidationConfig holds configuration related to data validation
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path  # Directory where validation results will be stored
    STATUS_FILE: str  # Path to the file where the validation status will be recorded
    ALL_REQUIRED_FILES: list  # List of required files that need to be present for validation

# DataTransformationConfig holds configuration related to data transformation
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path  # Directory where transformed data will be stored
    data_path: Path  # Path to the dataset that needs to be transformed
    tokenizer_name: Path  # Name of the pre-trained tokenizer used for data transformation

# ModelTrainerConfig holds configuration related to model training
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path  # Directory where model training artifacts will be stored
    data_path: Path  # Path to the dataset used for training
    model_ckpt: Path  # Path or name of the pre-trained model checkpoint to fine-tune
    num_train_epochs: int  # Number of epochs for training
    warmup_steps: int  # Number of warmup steps for the learning rate scheduler
    per_device_train_batch_size: int  # Batch size per device during training
    weight_decay: float  # Weight decay for optimization
    logging_steps: int  # Number of steps between logging
    evaluation_strategy: str  # Strategy for evaluation (e.g., 'steps')
    eval_steps: int  # Number of steps between evaluations
    save_steps: float  # Number of steps between saving checkpoints
    gradient_accumulation_steps: int  # Number of steps to accumulate gradients

# ModelEvaluationConfig holds configuration related to model evaluation
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path  # Directory where model evaluation results will be stored
    data_path: Path  # Path to the dataset used for evaluation
    model_path: Path  # Path to the trained model for evaluation
    tokenizer_path: Path  # Path to the tokenizer used with the model
    metric_file_name: Path  # Path to the file where evaluation metrics will be recorded
