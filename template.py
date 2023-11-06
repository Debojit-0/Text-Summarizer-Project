import os
from pathlib import Path # this path function converts the  / into respectove os meaning for eg home\destop\foldername this is windows
# where as in linux its like home/desktop/foldername
#so this converts the linux / to windows or viceversa
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "TextSumaarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]






for filepath in list_of_files:
    filepath = Path(filepath)
    #print(filepath)
    #so this is converting linux / to windows \
    filedir, filename = os.path.split(filepath)
    #print(filedir)
    #print(filename)

    if filedir !="":  #this means in this if we are creating the directory in the above loop we are reading the list of files and directory
        # so basically the list of directories that needs to be created are stored in filedir
        # so if the file directory is not empty or present in the filedir variable then create the directory
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory:{filedir} for the file{filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        # if the file path is not  existing or the file path i.e file size is zero the i will create the file
        # in the abpve if i created the directory here i am createing the file
        with open(filepath, 'w') as f:
            pass
        logging.info(f"creating file:{filepath}")
    
else:
    logging.info(f"{project_name} directory already exists")


