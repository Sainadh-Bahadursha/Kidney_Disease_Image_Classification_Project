import os
from pathlib import Path
import logging

# Configures logging to display INFO level messages with a timestamp
#logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# sets the project name.
project_name = 'kidney_disease_image_classification'

# Defines a list of file paths related to the project structure, including source files, configuration files, and dependencies.
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

# Iterates over the list of file paths and creates the necessary directories and files.
for filepath in list_of_files:
    # Convert the filepath to a Path object
    filepath = Path(filepath)
    
    # Get the directory and filename
    filedir, filename = os.path.split(filepath)
    
    # Create the directory if it does not exist 
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # Create the file if it does not exist
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    # Log a message if the file already exists
    else:
        logging.info(f"{filename} is already exists")
        