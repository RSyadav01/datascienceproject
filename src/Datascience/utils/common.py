import os
import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path 
from typing import Any
from box.exceptions import BoxValueError
from src.Datascience import logger  


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns a ConfigBox.

    Args:
        path_to_yaml (Path): Path to YAML file.

    Raises:
        ValueError: If YAML file is empty.
        Exception: For other errors.

    Returns:
        ConfigBox: Parsed YAML data.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of directories.

    Args:
        path_to_directories (list): List of directory paths.
        verbose (bool, optional): Whether to log directory creation. Defaults to True.
    """    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)    
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves data as a JSON file.

    Args:
        path (Path): Path to save JSON file.
        data (dict): Data to be saved.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads data from a JSON file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: JSON data as a ConfigBox object.
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves binary files.

    Args:
        data (Any): Data to be saved as binary.
        path (Path): Path to save binary file.
    """
    joblib.dump(data, path)  # Save the binary data
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads binary data.

    Args:
        path (Path): Path to the binary file.
    
    Returns:
        Any: Object stored in the file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data
