import pandas as pd

def analyze_single(df, area):
    return df[df["final location"].str.lower() == area.lower()]

def analyze_compare(df, a1, a2):
    return df[df["final location"].str.lower().isin([a1.lower(), a2.lower()])]
