import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

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

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())


    
    