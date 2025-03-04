import yaml
import os
from box import ConfigBox  
from src.Datascience.constants import *  
from src.Datascience.utils.common import read_yaml, create_directories
from src.Datascience.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from src.Datascience.entity.config_entity import (
    DataIngestionConfig, 
    DataValidationConfig,
    DataTransformationConfig, 
    ModelTrainerConfig, 
    ModelEvaluationConfig  
)

class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH,
                 schema_filepath=SCHEMA_FILE_PATH):
        """Initialize ConfigurationManager and read YAML configurations."""
    
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])  

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion  
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config


    def get_data_validation_config(self) -> DataValidationConfig:
        """Returns DataValidationConfig object with configuration values."""
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        """Returns DataTransformationConfig object with configuration values."""
        config = self.config.data_transformation
        create_directories([config.root_dir])

        return DataTransformationConfig(
            root_dir=config.root_dir,
            processed_data_dir=config.processed_data_dir,
            train_test_split_ratio=config.train_test_split_ratio,
            data_path=config.data_path 
        )

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir]) 
        
        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema.name
        )

        return model_trainer_config


    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params 
        schema = self.schema.TARGET_COLUMN
        
        target_column = schema.name
        all_params = params.to_dict() if hasattr(params, "to_dict") else dict(params)

        create_directories([config.root_dir])

        model_evaluation_config=ModelEvaluationConfig(
            root_dir=config.root_dir,
            model_path=config.model_path,
            test_data_path=config.test_data_path,
            metric_file_name=config.metric_file_name,  
            mlflow_uri="https://dagshub.com/RSyadav01/datascienceproject.mlflow",
            target_column=target_column,
            all_params=all_params
        )
        return model_evaluation_config

