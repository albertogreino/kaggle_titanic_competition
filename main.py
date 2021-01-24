from helpers.acquire_data import get_test_df, get_train_df
from helpers.train_summary import *
from helpers.correlation_two_variables import *
import pandas as pd


def main():
    train_df = get_train_df()
    test_df = get_test_df()

    # print_train_summary(train_df)
    # print_correlations()


def print_correlations():
    print_corr_between_two_vars(train_df, 'Pclass', 'Survived', 'Survived', False)
    print('\n')
    print_corr_between_two_vars(train_df, 'Sex', 'Survived', 'Survived', False)
    print('\n')
    print_corr_between_two_vars(train_df, 'SibSp', 'Survived', 'Survived', False)
    print('\n')
    print_corr_between_two_vars(train_df, 'Parch', 'Survived', 'Survived', False)


if __name__ == '__main__':
    main()
