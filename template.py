import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "src"


list_of_files = [

    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",

    f"{project_name}/config/configuration.py",

    f"{project_name}/entity/config_entity.py",

    f"{project_name}/exception/exception_handler.py",
    f"{project_name}/logger/log.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/util.py",
    "config/config.yaml",
    ".dockerignore",
    "app.py",
    "Dockerfile",
    "setup.py"


]


for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")


    if(not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filename}")


    else:
        logging.info(f"{filename} is already created")
