from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: Path  
    unzip_data_dir: Path
    all_schema: dict

# ✅ ADD THIS: DataTransformationConfig
@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    processed_data_dir: Path
    train_test_split_ratio: float


@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str

@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    metric_file_name: Path
    mlflow_uri: str 
    target_column: str
    all_params: dict

