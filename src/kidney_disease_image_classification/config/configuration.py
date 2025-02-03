from kidney_disease_image_classification.constants import *
from kidney_disease_image_classification.utils.common import read_yaml, create_directories
from kidney_disease_image_classification.entity.config_entity import (DataIngestionConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        # Reads the configuration and parameters from YAML files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Creates directories for the artifacts root
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # Retrieves data ingestion configuration from the loaded config
        config = self.config.data_ingestion

        # Creates necessary directories for data ingestion
        create_directories([config.root_dir])

        # Constructs and returns the DataIngestionConfig object
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config