import pandas as pd
import numpy as np

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    # --- Android_Version_Major ---
    # Tomamos la parte antes del primer punto y convertimos a int
    df['Android_Version_Major'] = df['Android_Version'].str.split(' ').str[0]

    # Convertimos a numérico (int), si falla dejamos NaN
    df['Android_Version_Major'] = pd.to_numeric(df['Android_Version_Major'], errors='coerce')

    # Creamos columnas de año y mes
    df['Last_Updated_Year'] = df['Last_Updated'].dt.year
    df['Last_Updated_Month'] = df['Last_Updated'].dt.month

    # Creamos una columna de rango de rating
    df['Rating_Group'] = pd.cut(
        df['Rating'],
        bins=[0, 2.5, 3.5, 4.5, 5],
        labels=['Low', 'Mid', 'High', 'Top']
    )

    return df