import os
import json
import joblib
from typing import Any
from pathlib import Path
from cnnClassifier import logger
from ensure import ensure_annotations
from box import ConfigBox
import yaml
from typing import List

@ensure_annotations
def read_yaml(path: Path)->ConfigBox:
    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
            logging.info(f"Yaml file read {path} succesfully")
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations  # Assuming ensure_annotations is defined appropriately
def create_directories(path_to_file: list, verbose=True):
    for path in path_to_file:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory {path} created")
        

@ensure_annotations
def get_size(path: Path)->str:
    size = os.path.getsize(path)
    logger.info(f"The size of the {path} is {size}")
    return size

@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,'w') as j:
        json.dump(data,j,indent=4)  
        logger.info(f"Json file {path} created") 


    
    