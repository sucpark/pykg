from numpy import random


def preprocess_df(df):

    new_df = df.drop_duplicates(ignore_index=True)
    new_df = new_df.dropna(axis=0)
    new_df = new_df.reset_index(drop=True)

    return new_df


def split_df(df, share=0.8, validation=True):
    mask = random.rand(len(df)) < share
    df_train = df[mask]
    df_test = df[~mask]
    df_valid = None

    if validation:
        mask = random.rand(len(df_test)) < 0.5  # we can set the validation share
        df_valid = df_test[mask]
        df_test = df_test[~mask]

    return df_train, df_valid, df_test
