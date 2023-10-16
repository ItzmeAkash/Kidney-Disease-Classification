# Kidney-Disease-Classification


## Workflows

1. Update Config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the Entity
5. Update the Configuration Manger in src config
6. Update the Components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. Last update the user interface app.py

# How to run?

### STEPS


Clone the repository

```bash
https://github.com/ItzmeAkash/Kidney-Disease-Classification
```

### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n kidney python=3.8 -y
```

```bash
conda activate kidney
```


### STEP 02- install the requirments

```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```






## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/itzmeakashps/Kidney-Disease-Classification.mlflow \
MLFLOW_TRACKING_USERNAME=itzmeakashps \
MLFLOW_TRACKING_PASSWORD=d587244e64e62ea9ab9a724d252a21ca83c524fe \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/itzmeakashps/Kidney-Disease-Classification.mlflow \

export MLFLOW_TRACKING_USERNAME=itzmeakashps 

export MLFLOW_TRACKING_PASSWORD=d587244e64e62ea9ab9a724d252a21ca83c524fe

```

### DVC cmd


1. dvc init
2. dvc repro
3. dvc dag
