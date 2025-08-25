import boto3
import os
from dotenv import load_dotenv
from src.constants import AWS_ACCESS_KEY_ID_ENV_KEY, AWS_SECRET_ACCESS_KEY_ENV_KEY, REGION_NAME

load_dotenv()


class S3Client:
    s3client = None
    s3resource = None

    def __init__(self, region_name = REGION_NAME):
        if S3Client.s3resource == None or S3Client.s3client == None:
            _access_key_id = os.getenv(AWS_ACCESS_KEY_ID_ENV_KEY, )
            _secret_access_key = os.getenv(AWS_SECRET_ACCESS_KEY_ENV_KEY, )

            # print(f"Id: {_access_key_id}")
            # print(f"Key: {_secret_access_key}")
            if _access_key_id is None:
                raise Exception(f"Environment Varialbe {AWS_ACCESS_KEY_ID_ENV_KEY} is not set.")
            if _secret_access_key is None:
                raise Exception(f"Envrironment Variable {AWS_SECRET_ACCESS_KEY_ENV_KEY} is not set.")
            
            S3Client.s3resource = boto3.resource('s3', aws_access_key_id = _access_key_id, aws_secret_access_key = _secret_access_key, region_name= region_name)

            S3Client.s3client = boto3.client('s3', aws_access_key_id = _access_key_id, aws_secret_access_key = _secret_access_key, region_name= region_name)

        self.s3client = S3Client.s3client
        self.s3resource = S3Client.s3resource

# if __name__ == "__main__":
#     s3 = S3Client()