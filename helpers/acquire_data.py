import pandas as pd


def get_train_df() -> pd.DataFrame:
    return pd.read_csv('../data/train.csv')


def get_test_df() -> pd.DataFrame:
    return pd.read_csv('../data/test.csv')
