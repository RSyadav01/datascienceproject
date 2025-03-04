import os
import urllib.request as request
import zipfile
from src.Datascience import logger
from src.Datascience.entity.config_entity import DataIngestionConfig, ModelTrainerConfig
from sklearn.linear_model import ElasticNet
import joblib
import pandas as pd

## Component - Data Ingestion
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    # Downloading the zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file  
            )
            logger.info(f"{filename} downloaded! with following info: \n{headers}")
        else:
            logger.info(f"File already exists")

    # Extract zip file
    def extract_zip_file(self):
        """
        Extracts the zip file.
        Function returns None.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)


## Component - Model Trainer
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        # Load training and test data
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

       
        target_column = str(self.config.target_column)  # Just access the string directly

        # Ensure target column exists in dataset
        if target_column not in train_data.columns:
            raise KeyError(f"Target column '{target_column}' not found in training data columns: {train_data.columns}")
        if target_column not in test_data.columns:
            raise KeyError(f"Target column '{target_column}' not found in test data columns: {test_data.columns}")

        # Split features and target
        train_x = train_data.drop(columns=[target_column])
        test_x = test_data.drop(columns=[target_column])
        train_y = train_data[target_column]
        test_y = test_data[target_column]

        # Train ElasticNet model
        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(train_x, train_y)

        # Save the model
        model_path = os.path.join(self.config.root_dir, self.config.model_name)
        joblib.dump(lr, model_path)
        logger.info(f"Model saved at {model_path}")
