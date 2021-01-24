import pandas as pd


def print_corr_between_two_vars(data_frame: pd.DataFrame,
                                main_var: str,
                                sec_var: str,
                                sorted_by=None,
                                ascending=True):
    sorted_by = sorted_by if sorted_by else main_var

    print(data_frame[[main_var, sec_var]]
          .groupby([main_var], as_index=False)
          .mean()
          .sort_values(by=sorted_by, ascending=ascending))
