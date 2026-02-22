import pandas as pd
import numpy as np


def clean(df: pd.DataFrame) -> pd.DataFrame:
    # estandarizamos Category
    df['Category'] = df['Category'].str.upper()
    df['Category'] = df['Category'].replace({
    'LIFESTYLE': 'HEALTH',
    'FINANCE': 'BUSINESS',
    'TOOLS': 'PRODUCTIVITY',
    'GAME': 'ENTERTAINMENT'
})

    # limpiamos la columna Installs
    df['Installs'] = df['Installs'].str.replace('+', '', regex=False)
    df['Installs'] = df['Installs'].str.replace(',', '', regex=False)
    df['Installs'] = df['Installs'].str.replace('installs', '', regex=False)
    df['Installs'] = df['Installs'].str.strip()
    df = df[df['Installs'] != 'unknown']
    df['Installs'] = df['Installs'].astype(int)

    # eliminamos las filas nulas ya que corresponden un 3% de la muestra total.
    df = df.dropna(subset=["Last_Updated"])

    # como en Rating hay valores nulos(48) vamos a transformar los nulos en la media de la columna
    df['Rating'] = round(df['Rating'].fillna(df['Rating'].mean()),1)

    # Genres tiene valores nulos y no esta estandarizado
    df['Genres'] = df['Genres'].str.upper()
    df['Genres'] = df['Genres'].fillna('UNKNOWN')

    # como Price_$ tiene valores nulos y asumiremos que las aplicaciones con precio nulo son gratuitas
    df['Price_$'] = df['Price_$'].fillna(0.0)

    # si el tipo es Free seteamos el precio a 0
    df['Price_$'] = np.where(df['Type'] == "Free", 0, df['Price_$'])

    # convertimos la columna Last_Updated a formato fecha
    df['Last_Updated'] = pd.to_datetime(df['Last_Updated'])
    
    # eliminamos la columna Size_MB ya que no aporta información relevante para el análisis, todos sus valores con 2.5 MB
    df.drop(columns=['Size_MB'], inplace=True)

    return df