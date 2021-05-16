import argparse
import pathlib
import yaml
import pandas as pd
import joblib
import os

from typing import Text
from src.train.train import train

def train_model(config_path: Text) -> None:
    """ Train model
    args:
        config_path {Text}: path to config
    """

    config = yaml.safe_load(open(config_path))

    train_df = pd.read_csv(config['data_split']["train_path"])
    target_column = config['featurize']['target_column']

    estimator_name = config['train']['estimator_name']
    param_grid = config['train']['estimators'][estimator_name]['param_grid']
    cv = config['train']['cv']

    model = train(
        df=train_df,
        target_column=target_column,
        estimator_name=estimator_name,
        param_grid=param_grid,
        cv=cv
    )
    print(model.best_score_)

    model_path = config['model']['model_path']
    pathlib.Path(model_path).mkdir(parents=True, exist_ok=True)

    model_name = config['model']['model_name']

    joblib.dump(
        model,
        os.path.join(model_path, model_name)
    ) 

if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--config", dest="config", required=True)
    args = args_parser.parse_args()

    train_model(config_path=args.config)

