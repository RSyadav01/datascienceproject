from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:  # Correct name
    root_dir: Path
    STATUS_FILE: Path  
    unzip_data_dir: Path
    all_schema: dict
