import argparse
from typing import Text
import yaml
import pathlib

from src.data.dataset import get_data

def data_load(config_path: Text) -> None:
    """ Load raw data.
    Args: 
        config_path {Text}: path to config
    """
    config = yaml.safe_load(open(config_path))
    pathlib.Path(config['data']['data_path']).mkdir(parents=True, exist_ok=True)
    pathlib.Path(config['data']['raw_data']).mkdir(parents=True, exist_ok=True)
    dataset = get_data()
    dataset.to_csv(config['data_load']['dataset_csv'], index=False)

if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    data_load(config_path=args.config)