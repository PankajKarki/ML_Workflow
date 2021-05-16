# Machine Learning pipeline with DVC

## Directory Structure

------------------------
```
.
├── api
├── data
├── models
├── notebooks
├── reports
└── src
    ├── data
    │   └── dataset.py
    ├── evaluate
    │   └── evaluate.py
    ├── features
    │   └── features.py
    ├── pipelines
    │   ├── data_load.py
    │   ├── data_split.py
    │   ├── evaluate.py
    │   ├── featurize.py
    │   └── train.py
    ├── report
    │   └── visualize.py
    └── train
        └── train.py
```

## Preparation

### 1. Fork / Clone this repository

```bash
git clone https://github.com/PankajKarki/ML_Workflow.git
cd ML_Workflow
```

### 2. Create and activate virtual environment

Create virtual environment named `dvc-venv` (you may use other name)
```bash
python3 -m venv env
echo "export PYTHONPATH=$PWD" >> env/bin/activate
source dvc-venv/bin/activate
pip install --upgrade pip
```
Install python libraries

```bash
pip install -r requirements.txt
```
To run pipeline

```bash
dvc repro
```

To visualize pipeline

```bash
dvc dag
```

## References for code examples used

1. [DVC tutorial](https://dvc.org/doc/tutorial)
2. [Machine Learning REPA](https://github.com/mlrepa)
3. [Machine Learning REPA Global](https://mlrepa.com/) 

