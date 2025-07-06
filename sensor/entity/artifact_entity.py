

from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    feature_store_file_path:str
    train_file_path:str 
    test_file_path:str

@dataclass    
class DataValidationConfig:
    report_file_path:str


class DataTransformationConfig:...   
class ModelTrainerConfig:...
class ModelEvaluationConfig:...
class ModelPusherConfig:...