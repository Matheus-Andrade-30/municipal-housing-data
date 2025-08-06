import pandas as pd

def carregar_csv(caminho, sep=","):
    return pd.read_csv(caminho, sep=sep)

def limpar_colunas(df):
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df