import os
import numpy as np
import sys
import dill
import yaml
from pandas import DataFrame
from src.exception import MyException


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