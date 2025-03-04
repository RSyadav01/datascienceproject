import pandas as pd
import os
from src.Datascience import logger
from sklearn.linear_model import ElasticNet
import joblib
import mlflow
from urllib.parse import urlparse
import dagshub  # type: ignore

from src.Datascience.entity.config_entity import ModelTrainerConfig

# Initialize DagsHub MLflow tracking
dagshub.init(repo_owner="RSyadav01", repo_name="networksecurity", mlflow=True)

# Set environment variables securely (avoid hardcoding sensitive information)
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/RSyadav01/datascienceproject/networksecurity.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "RSyadav01"  
os.environ["MLFLOW_TRACKING_PASSWORD"] = "ba113154bebffe15197f45c072017bb503668fa9" 

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        # Initialize MLflow tracking
        mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
        mlflow.set_experiment("ElasticNet_Model_Training")

        with mlflow.start_run():
            # Define model
            lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
            
            # Train model
            lr.fit(train_x, train_y)

            # Log model parameters
            mlflow.log_param("alpha", self.config.alpha)
            mlflow.log_param("l1_ratio", self.config.l1_ratio)

            # Log training metrics (optional, you can add more)
            train_score = lr.score(train_x, train_y)
            test_score = lr.score(test_x, test_y)

            mlflow.log_metric("train_score", train_score)
            mlflow.log_metric("test_score", test_score)

            # Log the model with an input example to avoid MLflow warning
            input_example = train_x.iloc[:1]  # Take one sample as input example
            mlflow.sklearn.log_model(lr, "model", input_example=input_example)

            # Save model locally
            joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))

        logger.info(f"Model saved at {os.path.join(self.config.root_dir, self.config.model_name)}")
