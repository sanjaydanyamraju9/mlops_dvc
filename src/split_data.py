import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from get_data import read_params, get_data
from load_data import load_and_save


def split_data(config_path):
    config = read_params(config_path)
    raw_df = pd.read_csv(config['load_data']['raw_dataset_csv'],sep=",")
    train_path = config['split_data']['train_path']
    test_path = config['split_data']['test_path']
    test_size = config['split_data']['test_size']
    random_state = config['base']['random_state']
    # target_col = config['base']['target_col']
    train,test= train_test_split( raw_df, test_size=test_size,random_state=random_state)
    train.to_csv(train_path, sep=',', index=False)
    test.to_csv(test_path, sep=',', index=False)


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args = args.parse_args()
    config_path = parsed_args.config
    split_data(config_path)

  