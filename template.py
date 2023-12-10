import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
project_name = "cnnClassifier"

list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/prepare_base_model.py",
    f"src/{project_name}/components/model_training.py",
    f"src/{project_name}/components/model_evaluation_mlflow.py",
    f"src/{project_name}/pipeline/data_ingestion.py",
    f"src/{project_name}/pipeline/prepare_base_model.py",
    f"src/{project_name}/pipeline/model_training.py",
    f"src/{project_name}/pipeline/model_evaluation_mlflow.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"config/config.yaml",
    "params.yaml",
    "setup.py",
    "main.py",
    "app.py",
    "dvc.yaml",
    "requirements.txt"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, filename = os.path.split(filepath)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Folder {file_dir} created for filename {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"Creating empty file")
    else:
        logging.info(f"File {filepath} already created")