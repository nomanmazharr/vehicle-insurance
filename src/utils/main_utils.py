import os
import numpy as np
import sys
import dill
import yaml
from pandas import DataFrame
from src.exception import MyException
from src.logger import logging


def read_yaml(file_path: str) -> dict:
    try:
        with open(file_path, 'rb') as f:
            return yaml.safe_load(f)
    except Exception as e:
        raise MyException(e, sys) from e
    

def write_yaml(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)        
        with open(file_path, 'wb') as f:
            yaml.dump(content, f)
    
    except Exception as e:
        raise MyException(e, sys) from e

def load_object(filepath: str) -> object:
    try:
        with open(filepath, 'rb') as f:
            obj = dill.load(f)
        return obj
    except Exception as e:
        raise MyException(e, sys) from e
    
def save_numpy_array_data(file_path: str, array:np.array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as f:
            np.save(f, array)
    except Exception as e:
        raise MyException(e, sys) from e
def load_numpy_array_data(filepath: str)-> np.array:
    try:
        with open(filepath, 'rb') as f:
            return np.load(f)
    except Exception as e:
        raise MyException(e, sys) from e
    
def save_object(filepath: str, obj: object) -> None:
    try:
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'wb') as f:
            dill.dump(obj, f)

        logging.info("Exited the save object method of utils")

    except Exception as e:
        raise MyException(e, sys) from e
        