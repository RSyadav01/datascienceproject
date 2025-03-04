from src.Datascience import logger
from src.Datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.Datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.Datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline  
from src.Datascience.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.Datascience.pipeline.model_evaluation_pipeline import ModelEvaluationTrainingPipeline  # ✅ Fixed Import

# ✅ Stage 1: Data Ingestion
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx========x")
except Exception as e:
    logger.exception(f"Exception occurred in {STAGE_NAME}: {e}")
    raise e

# ✅ Stage 2: Data Validation
STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()  # ✅ Correct method name
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(f"Exception occurred in {STAGE_NAME}: {e}")
    raise e

# ✅ Stage 3: Data Transformation
STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()  
    data_transformation.initiate_data_transformation()  
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(f"Exception occurred in {STAGE_NAME}: {e}")
    raise e

STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = ModelTrainerTrainingPipeline()
    data_ingestion.initiate_model_training()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model evaluation stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = ModelEvaluationTrainingPipeline()
    data_ingestion.initiate_model_evaluation()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
