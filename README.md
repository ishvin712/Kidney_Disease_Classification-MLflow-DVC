# Kidney_Disease_Classification-MLflow-DVC


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. Update the app.py

# How to run?

### STEPS:

Clone the repository 

```bash
https://github.com/ishvin712/Kidney_Disease_Classification-MLflow-DVC
```
### STEP 01- Create a conda enviornment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```




## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/ishvin712/Kidney_Disease_Classification-MLflow-DVC.mlflow \
MLFLOW_TRACKING_USERNAME=ishvin712 \
MLFLOW_TRACKING_PASSWORD=b417bbd9ea6d4467a047c2c36809e3bcd7b97596 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/ishvin712/Kidney_Disease_Classification-MLflow-DVC.mlflow

export MLFLOW_TRACKING_USERNAME= ishvin712

export MLFLOW_TRACKING_PASSWORD=b417bbd9ea6d4467a047c2c36809e3bcd7b97596

```
