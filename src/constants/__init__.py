import os
from datetime import date


# For MongoDB connection
DATABASE_NAME = "vehicleinsurace"
COLLECTION_NAME = "vehicle"
MONGODB_URL_KEY = "MONGO_URI"

PIPELINE_NAME: str = ""
ARTIFACT_DIR: str = "artifact"


MODEL_FILE_NAME ="model.pkl"


PREPROCESSING_OBJECT_FILE_NAME = 'preprocessing.pkl'
TARGET_COLUMN: str = "Response"
CURRENT_YEAR = date.today().year

FILE_NAME: str = "data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml") 


# AWS Credentials
AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"
REGION_NAME = "us-east-1"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "vehicle"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.25


# Data Validation related constants
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_REPORT_FILE_NAME: str = "report.yaml"

# Data pre-processing related constants
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = 'transformed'
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"


# Model Trainer related constants
MODEL_TRAINER_DIR_NAME: str = 'model_trainer'
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")
MODEL_TRAINER_N_ESTIMATORS = 100
MODEL_TRAINER_MIN_SAMPLES_SPLIT: int = 3
MODEL_TRAINER_MIN_SAMPLES_LEAF: int = 2
MIN_SAMPLES_SPLIT_MAX_DEPTH: int = 5
MIN_SAMPLES_SPLIT_CRITERION: str = 'entropy'
MIN_SAMPLES_SPLIT_RANDOM_STATE: int = 42


# Model Evaluation related constants
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02
MODEL_BUCKET_NAME = 'vehicle-insurance-model-data'
MODEL_PUSHER_S3_KEY = 'model-registry'