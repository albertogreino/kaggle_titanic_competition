import pandas as pd


def print_train_summary(data_frame: pd.DataFrame):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    data_frame.info()
    print("- " * 40)
    print(data_frame.describe())
