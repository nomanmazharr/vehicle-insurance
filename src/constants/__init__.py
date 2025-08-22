import os
from datetime import date


# For MongoDB connection
DATABASE_NAME = "vehicleinsurace"
COLLECTION_NAME = "vehicle"
MONGODB_URL_KEY = "MONGO_URI"

PIPELINE_NAME: str = ""
ARTIFACT_DIR: str = "artifact"

PREPROCESSING_OBJECT_FILE_NAME = 'preprocessing.pkl'
TARGET_COLUMN: str = "Response"
CURRENT_YEAR = date.today().year

FILE_NAME: str = "data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml") 

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