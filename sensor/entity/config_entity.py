import os,sys
from sensor.exception import SensorException
from sensor.logger import logging
from datetime import datetime

class TrainingPipelineConfig:

    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%I%M%S_%p')}")
        except Exception  as e:
            raise SensorException(e,sys)    



class DataIngestionConfig:
   
class DataValidationConfig:...
class DataTransformationConfig:...   
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...