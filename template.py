import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "uber"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/uber/__init__.py",
    f"src/uber/components/__init__.py",
    f"src/uber/components/data_ingestion/__init__.py",
    f"src/uber/components/data_transformation/__init__.py",
    f"src/uber/components/model_trainer/__init__.py",
    f'src/uber/components/model_monitoring/__init__.py',
    f"src/uber/pipeline/__init__.py",
    f"src/uber/pipeline/training_pipeline.py",
    f"src/uber/pipeline/prediction_pipeline.py",
    f"src/uber/exception.py",
    f"src/uber/logger.py",
    f"src/uber/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",  
]


# logging ra , kete code, lekhibaku padhiba 
