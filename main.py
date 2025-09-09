from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import sys
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainPipelineConfig

if __name__=="__main__":
    try:
        trainpipelineconfig = TrainPipelineConfig()
        data_ingestion_config = DataIngestionConfig(trainpipelineconfig)
        networkobj = DataIngestion(data_ingestion_config)
        path = networkobj.initiate_data_ingestion()
        print(path)

    except Exception as e:
        raise NetworkSecurityException(e,sys)
