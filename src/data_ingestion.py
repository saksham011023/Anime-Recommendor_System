import os
import pandas as pd
from google.cloud import storage
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml

logger=get_logger(__name__)

class DataIngestion:
    def __init__(self,config):
        
        self.config=config["data_ingestion"]
        self.bucket_name=self.config["bucket_name"]
        self.file_names=self.config["bucket_file_names"]
        
        os.makedirs(RAW_DIR,exist_ok=True)
        
        logger.info("Data Ingestion started....")

    def download_csv_from_gcp(self):

        try:

            client=storage.Client()
            bucket=client.bucket(self.bucket_name)

            for filename in self.file_names:
                file_path=os.path.join(RAW_DIR,filename)

                if filename=="animelist.csv":
                    blob=bucket.blob(filename)
                    blob.download_to_filename(file_path)

                    data=pd.read_csv(file_path,nrows=7000000)
                    data.to_csv(file_path,index=False)
                    logger.info("Large File detected. Only Downloading 7M rows")

                else:
                    blob=bucket.blob(filename)
                    blob.download_to_filename(file_path)
                    logger.info("Downloading smaller files.. ")
        
        except Exception as e:
            logger.error(f"Error while downloading data from GCP")
            raise CustomException("Failed to download data",e)
    
    def run(self):
        try:
            logger.info("Starting Data Ingestion process...")
            self.download_csv_from_gcp()
            logger.info("Data Ingestion completed...")
        
        except CustomException as ce:
            logger.error(f"CustomExceptioin : {str(ce)}")
        
        finally:
            logger.info("DATA INGESTION DONE...")

if __name__=="__main__":
    data_ingestion=DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()
    