import os
from src.Datascience import logger
import pandas as pd
from src.Datascience.entity.config_entity import DataValidationConfig



class DataValidation:
    def __init__(self, config:DataValidationConfig): 
        self.config = config


    def validate_all_columns(self) -> bool:
        """Validate if all required columns exist in the dataset."""
        try:
            validation_status = None  # Initialize validation status

            # Read CSV data
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)  # Extract column names

            # Get expected schema columns
            all_schema = self.config.all_schema.keys()

            # Check if all columns exist in the schema
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            else:
                validation_status = True
                  # Write validation status to the status file
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e
         
