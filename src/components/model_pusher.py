import sys
from src.cloud_storage.aws_storage import SimpleStorageService
from src.exception import MyException
from src.entity.artifact_entity import ModelPusherArtifact, ModelEvaluationArtifact
from src.logger import logging
from src.entity.config_entity import ModelPusherConfig
from src.entity.s3_estimator import VehicleInsuraceEstimator

class ModelPusher: 
    def __init__(self, model_evaluation_artifact: ModelEvaluationArtifact, model_pusher_config: ModelPusherConfig):
        self.s3 = SimpleStorageService()
        self.model_evaluation_artifact = model_evaluation_artifact
        self.model_pusher_config = model_pusher_config
        self.vehicle_estimator = VehicleInsuraceEstimator(bucket_name=model_pusher_config.bucket_name, model_path=model_pusher_config.s3_model_key_path)

    def initiate_model_pusher(self) -> ModelPusherArtifact:
        try:
            
            print("------------------------------------------------------------------------------------------------")
            logging.info("Uploading artifacts to s3 bucket")

            logging.info('uploading new model to s3 bucket')
            self.vehicle_estimator.save_model(from_file=self.model_evaluation_artifact.trained_model_path)
            model_pusher_artifact = ModelPusherArtifact(bucket_name=self.model_pusher_config.bucket_name, s3_model_path=self.model_pusher_config.s3_model_key_path) 

            logging.info("Uploaded artifacts folder to s3 bucket")
            logging.info(f"Model pusher artifact: [{model_pusher_artifact}]")
            logging.info("Exited initiate_model_pusher method of ModelTrainer class")

            return model_pusher_artifact
        
        except Exception as e:
            raise MyException(e, sys) from e
