from helpers.acquire_data import get_test_df, get_train_df
import pandas as pd


def main():
    train_df = get_train_df()
    test_df = get_test_df()

    train_df.info()
    print('_' * 40)
    test_df.info()
if __name__ == '__main__':
    main()
