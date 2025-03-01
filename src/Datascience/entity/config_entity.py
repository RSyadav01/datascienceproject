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
