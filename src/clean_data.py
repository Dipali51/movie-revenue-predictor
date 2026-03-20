# src/clean_data.py
import pandas as pd

def load_and_clean(path):
    df = pd.read_csv(path)
    df = df[["budget", "popularity", "runtime", "vote_average", "vote_count", "revenue"]]
    df = df[(df["budget"] > 0) & (df["revenue"] > 0)]
    df.dropna(inplace=True)
    return df
