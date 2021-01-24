from helpers.acquire_data import get_test_df, get_train_df
from helpers.train_summary import *
import pandas as pd


def main():
    train_df = get_train_df()
    test_df = get_test_df()

    print_train_summary(train_df)

if __name__ == '__main__':
    main()
