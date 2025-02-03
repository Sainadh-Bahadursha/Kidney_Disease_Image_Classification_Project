from kidney_disease_image_classification.config.configuration import ConfigurationManager
from kidney_disease_image_classification.components.data_ingestion import DataIngestion
from kidney_disease_image_classification import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Loads configuration and sets up data ingestion
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        
        # Initializes and runs the data ingestion process
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()  # Downloads data file
        data_ingestion.extract_zip_file()  # Extracts the downloaded zip file

if __name__ == '__main__':
    try:
        # Logs the start of the data ingestion stage
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        
        # Executes the main pipeline for data ingestion
        obj = DataIngestionTrainingPipeline()
        obj.main()
        
        # Logs the completion of the data ingestion stage
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Logs and raises any exceptions that occur
        logger.exception(e)
        raise e
