import pandas as pd


def clean(df: pd.DataFrame) -> pd.DataFrame:
    df['Category'] = df['Category'].str.upper()

    df['Installs'] = df['Installs'].str.replace('+', '', regex=False)
    df['Installs'] = df['Installs'].str.replace(',', '', regex=False)
    df['Installs'] = df['Installs'].str.replace('installs', '', regex=False)
    df['Installs'] = df['Installs'].str.strip()

    return df