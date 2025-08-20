import sys
import pandas as pd
import numpy as np
from typing import Optional

from src.configuration.mongo_db_connections import MongoDBClient
from src.constants import DATABASE_NAME
from src.exception import MyException
from src.logger import logging

class VehicleDataAccess:

    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise MyException(e, sys)
        
    def export_collection_as_df(self, collection_name:str, database_name:Optional[str]=None)-> pd.DataFrame:
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]

            else:
                collection = self.mongo_client[database_name][collection_name]

            logging.info('Fetching data from Mongodb')
            df = pd.DataFrame(list(collection.find()))
            logging.info(f"Length of Total data is: {len(df)}")
            if 'id' in df.columns.to_list():
                df = df.drop('id', axis=1)
            df.replace({"na":np.nan}, inplace=True)
            return df
        
        except Exception as e:
            MyException(e, sys)


# if __name__ == "__main__":
#     data = VehicleDataAccess()

#     df = data.export_collection_as_df(collection_name='vehicle')