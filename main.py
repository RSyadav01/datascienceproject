from src.Datascience import logger
from src.Datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.Datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.Datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline  
from src.Datascience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline

# ✅ Stage 1: Data Ingestion
STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

# ✅ Stage 2: Data Validation
STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()  # ✅ Correct method name
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

# ✅ Stage 3: Data Transformation
STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()  
    data_transformation.initiate_data_transformation()  
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    
    trainer_pipeline = ModelTrainerTrainingPipeline()
    trainer_pipeline.initiate_model_training()
    
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e

