import os
from get_data import read_params, get_data
import argparse


def load_and_save(config_path):
    config = read_params(config_path)
    df = get_data(config_path)
    columns = [col.replace(" ","_") for col in df.columns]
    print(columns)
    raw_data_path = config['load_data']['raw_dataset_csv']
    df.to_csv(raw_data_path, sep=',', index=False, header = columns)

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    config_path = parsed_args.config
    load_and_save(config_path)
    
