from text_summarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline  # Importing Data Ingestion pipeline class
from text_summarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline  # Importing Data Validation pipeline class
from text_summarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline  # Importing Data Transformation pipeline class
from text_summarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline  # Importing Model Trainer pipeline class
from text_summarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline  # Importing Model Evaluation pipeline class (commented out)
from text_summarizer.logging import logger  # Importing logger for logging

# Stage: Data Ingestion
STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")  # Log the start of Data Ingestion stage
    data_ingestion = DataIngestionTrainingPipeline()  # Initialize Data Ingestion pipeline
    data_ingestion.main()  # Execute the Data Ingestion pipeline
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")  # Log the completion of Data Ingestion stage
except Exception as e:
    logger.exception(e)  # Log any exception that occurs
    raise e  # Re-raise the exception for further handling

# Stage: Data Validation
STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")  # Log the start of Data Validation stage
    data_validation = DataValidationTrainingPipeline()  # Initialize Data Validation pipeline
    data_validation.main()  # Execute the Data Validation pipeline
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")  # Log the completion of Data Validation stage
except Exception as e:
    logger.exception(e)  # Log any exception that occurs
    raise e  # Re-raise the exception for further handling

# Stage: Data Transformation
STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")  # Log the start of Data Transformation stage
    data_transformation = DataTransformationTrainingPipeline()  # Initialize Data Transformation pipeline
    data_transformation.main()  # Execute the Data Transformation pipeline
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")  # Log the completion of Data Transformation stage
except Exception as e:
    logger.exception(e)  # Log any exception that occurs
    raise e  # Re-raise the exception for further handling

# Stage: Model Trainer
STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f"*******************")  # Log a separator for clarity
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")  # Log the start of Model Trainer stage
    model_trainer = ModelTrainerTrainingPipeline()  # Initialize Model Trainer pipeline
    model_trainer.main()  # Execute the Model Trainer pipeline
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")  # Log the completion of Model Trainer stage
except Exception as e:
    logger.exception(e)  # Log any exception that occurs
    raise e  # Re-raise the exception for further handling

# Stage: Model Evaluation
STAGE_NAME = "Model Evaluation stage"
try:
    logger.info(f"*******************")  # Log a separator for clarity
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")  # Log the start of Model Evaluation stage
    model_evaluation = ModelEvaluationTrainingPipeline()  # Initialize Model Evaluation pipeline
    model_evaluation.main()  # Execute the Model Evaluation pipeline
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")  # Log the completion of Model Evaluation stage
except Exception as e:
    logger.exception(e)  # Log any exception that occurs
    raise e  # Re-raise the exception for further handling
