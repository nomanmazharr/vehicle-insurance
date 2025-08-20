import pymongo
import sys
import certifi
import os
from dotenv import load_dotenv

from src.exception import MyException
from src.logger import logging
from src.constants import MONGODB_URL_KEY, DATABASE_NAME


ca = certifi.where()
load_dotenv()

class MongoDBClient():
    """Creating connection to our MongoDB"""

    client = None
    
    def __init__(self, database_name: str= DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_uri = os.getenv(MONGODB_URL_KEY)
                if mongo_uri is None:
                    raise Exception(f"Environment variable '{MONGODB_URL_KEY}' is not set.")
                
                MongoDBClient.client = pymongo.MongoClient(mongo_uri, tlsCAfile=ca)
            
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB Connection Successful")

        except Exception as e:
            raise MyException(e, sys)



# if __name__ == "__main__":
#     try:
#         db_client = MongoDBClient(database_name=DATABASE_NAME)

#         print("Connection successful")
#     except Exception as e:
#         print(f"Exception: {e}")