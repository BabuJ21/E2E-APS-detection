from sensor.entity import artifact_entity, config_entity
from sensor.exception import SensorException
from sensor.logger import logging
from scipy.stats import ks_2samp
import os, sys


class DataValidation:
    
    def __init__(self,data_validation_config:config_entity.DataValidationConfig):
        try:
            logging.info(f"{'>>'*20} Data Validation {'<<'*20}")
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise SensorException(e, sys)
    
    def is_required_columns_exists(self,)->bool:
        pass

    def drop_missing_columns(self):
        pass


    def initiate_data_validation(self) -> artifact_entity.DataValidationArtifact:
        pass

