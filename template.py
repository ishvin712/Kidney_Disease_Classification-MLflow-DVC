import os
from pathlib import Path
import logging 

#logging string 
# works like print statement but is logged

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifer' 

list_of_files = {
    ".github/workflows/.gitkeep", #gitkeep - when pushing content on github , empty files are not pushed 
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/componenets/__init__.py",
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
}   

for filepath in list_of_files:
    filepath = Path(filepath) #Path class is given to convert the path fot windows OS ( backslash format)
    filedir, filename = os.path.split(filepath) # split the folders and files

    if filedir!= "":
        os.makedirs(filedir, exist_ok=True) # to create folder 
        logging.info(f"Creating directory; {filedir} for the file {filename}")
    
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} already exists")
