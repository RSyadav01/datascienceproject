import yaml
import os
from src.Datascience.constants import *
from src.Datascience.utils.common import read_yaml, create_directories
from src.Datascience.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from src.Datascience.entity.config_entity import DataIngestionConfig, DataValidationConfig,DataTransformationConfig,ModelTrainerConfig


# Define read_yaml function if not imported from utils
def read_yaml(filepath):
    """Reads a YAML file and returns the parsed data."""
    with open(filepath, 'r') as file:
        return yaml.safe_load(file)


# Define create_directories function if not imported from utils
def create_directories(dirs):
    """Creates directories if they do not exist."""
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)


class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH,
                 schema_filepath=SCHEMA_FILE_PATH):
        """Initialize ConfigurationManager and read YAML configurations."""
    
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config['artifacts_root']])  

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """Returns DataIngestionConfig object with configuration values."""
        config = self.config['data_ingestion']  
        create_directories([config['root_dir']])

        return DataIngestionConfig(
            root_dir=config['root_dir'],
            source_url=config['source_url'],
            local_data_file=config['local_data_file'],
            unzip_dir=config['unzip_dir']
        )

    def get_data_validation_config(self) -> DataValidationConfig:
        """Returns DataValidationConfig object with configuration values."""
        config = self.config['data_validation']
        schema = self.schema['COLUMNS']

        create_directories([config['root_dir']])

        return DataValidationConfig(
            root_dir=config['root_dir'],
            STATUS_FILE=config['STATUS_FILE'],
            unzip_data_dir=config['unzip_data_dir'],
            all_schema=schema
        )

    def get_data_transformation_config(self) -> DataTransformationConfig:
        """Returns DataTransformationConfig object with configuration values."""
        config = self.config['data_transformation']
        create_directories([config['root_dir']])

        return DataTransformationConfig(
            root_dir=config['root_dir'],
            processed_data_dir=config['processed_data_dir'],
            train_test_split_ratio=config['train_test_split_ratio'],
            data_path=config['data_path'] 
        )

    def get_model_trainer_config(self) ->ModelTrainerConfig:
        config = self.config['model_trainer'] 

        params = self.params['ElasticNet']  

        schema = self.schema['TARGET_COLUMN'] 

        create_directories([config['root_dir']]) 
        
        model_trainer_config = ModelTrainerConfig(
    root_dir=config['root_dir'],
    train_data_path=config['train_data_path'],
    test_data_path=config['test_data_path'],
    model_name=config['model_name'],
    alpha=params['alpha'],
    l1_ratio=params['l1_ratio'],
    target_column=schema['name']
)

        return model_trainer_config
