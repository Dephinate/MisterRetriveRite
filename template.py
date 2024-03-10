"""
Process:
1) Create a List of what files you want to create
2) Create directories first
3) Create files after step 2. While creating check if the file is empty to avoid recreating of files
"""

# Import Libraries
import os
from pathlib import Path
import logging

# Initalize logger

logging.basicConfig( # basicConfig configures the logging system
    level=logging.INFO, 
    format='[%(asctime)s]: %(message)s:'
    )

project_name = "misterRetriveRite"

# Declare a list of driectrories and files

list_of_files = [
    ".github/workflows/.gitkeep", # .github is for CI/CD deployment, .gitkeep is a hidden file included as we cannot upload an empty folder. Whenever we will do a commit
                                  # it will automatically take it from github and do the deployment over to the cloud
    f"src/{project_name}/__init__.py", # this constructor file is create a local package so we can do something like- from TextSummarizer import something
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configurations.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml", # model related parameters
    "app.py",
    "main.py", 
    "DockerFile", # for EC2 deployment
    "requirements.txt", # environment setup
    "setup.py",
    "research/trials.ipynb" # for R&D

]

# Loop through the list to create files and folders

for filepath in list_of_files:
    filepath = Path(filepath) # use Path to make path platform independent( forward slash in windows and back slash in ubuntu)
    filedir,filename = os.path.split(filepath)

    # First create directory and then create file
    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating directory {filedir} for the file {filename}")

    if (not os.path.exists(filepath) or os.path.getsize(filepath)==0): # check size of files to avoid recreating them
        with open(filepath,'w') as f:
            pass
        logging.info(f"Creating empty file {filename}")

    else:
        logging.info(f"{filename} already exists")


