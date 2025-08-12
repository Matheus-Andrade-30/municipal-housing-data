import pandas as pd

def carregar_csv(caminho, sep=","):
    return pd.read_csv(caminho, sep=sep)

def limpar_colunas(df):
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    return df

def dados_limpos_Total(df: pd.DataFrame) -> pd.DataFrame:
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

def dados_limpos_Situacao(df: pd.DataFrame) -> pd.DataFrame:
    df.rename(columns={
    'Domicílio': 'domicilio',
    'Regiao' : 'regiao',
    'Domicílios Rústicos' : 'domicilios_rusticos',
    'Domicílios Improvisados' : 'domicilios_improvisados',
    'Habitação Precária' : 'habitacao_precaria',
    'Cômodos' : 'comodos',
    'Unidades conviventes déficit' : 'unidades_conviventes_deficit',
    'Coabitação' : 'coabitacao',
    'Ônus' : 'onus',
    'Déficit Habitacional (Habitação Precária + Coabitação + Ônus)' : 'deficit_original'
    }, inplace=True)

    colunas_excluir = ["regiao", "domicilio"]

    colunas_converter = [col for col in df.columns if col not in colunas_excluir]

    for col in colunas_converter:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace('.', '', regex=False)
            .str.replace(',', '.', regex=False)
        )
    df[col] = pd.to_numeric(df[col], errors='coerce')
    df['onus'] = df['onus'].fillna(0)

    df['deficit_total'] = df['habitacao_precaria'] + df['coabitacao'] + df['onus']
    df.drop(columns=['N', 'deficit_original'], inplace=True)

    df_regioes = df[df['regiao'] != 'Brasil'].copy()
    df_brasil = df[df['regiao'] == 'Brasil'].copy()

    return df_regioes, df_brasil
