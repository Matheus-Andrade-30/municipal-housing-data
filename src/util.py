import pandas as pd

def carregar_csv(caminho, sep=","):
    return pd.read_csv(caminho, sep=sep)

def limpar_colunas(df):
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df

def dados_limpos(df: pd.DataFrame) -> pd.DataFrame:
    df = df[df["Região"] != "Brasil"]

    novos_nomes = [
    "regiao", "rusticos", "improvisados", "habitacao_precaria", "comodos",
    "unidade_convivente_deficit", "coabitacao", "onus", "deficit_habitacional"
    ]

    df = df.iloc[:, :len(novos_nomes)]  
    df.columns = novos_nomes
    colunas_excluir = ["regiao", "rusticos"]

    colunas_converter = [col for col in df.columns if col not in colunas_excluir]

    for col in colunas_converter:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace(".", "", regex=False) 
            .str.replace(",", ".", regex=False) 
        )
        df[col] = pd.to_numeric(df[col], errors="coerce")

    return df