'''
1) read yaml
2) create directory

'''

import os
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
import yaml
from misterRetriveRite.logging import logger

@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            return (ConfigBox(content))
    except BoxValueError:
        raise ValueError("yaml is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directory(path_to_directories: list, verbose = True):
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"created directory at: {path}")

    except Exception as e:
        raise e
    
@ensure_annotations
def create_file(file_names: list, verbose = True):
    try:
        for file in file_names:
            with open(file,'w') as f:
                pass
            if verbose:
                    logger.info(f"created file : {file}")
    
    except Exception as e:
        raise e