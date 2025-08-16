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


def dados_limpos_Sexo_do_Responsavel(df: pd.DataFrame) -> pd.DataFrame:
    df.rename(columns={
    'Regiao' : 'regiao',
    'Sexo' : 'sexo',
    'Domicílios Rústicos' : 'domicilios_rusticos',
    'Domicílios Improvisados' : 'domicilios_improvisados',
    'Habitação Precária' : 'habitacao_precaria',
    'Cômodos' : 'comodos',
    'Unidades conviventes déficit' : 'unidades_conviventes_deficit',
    'Coabitação' : 'coabitacao',
    'Ônus' : 'onus',
    'Déficit Habitacional (Habitação Precária + Coabitação + Ônus)' : 'deficit_original'
    }, inplace=True)

    colunas_excluir = ["regiao", "sexo"]

    colunas_converter = [col for col in df.columns if col not in colunas_excluir]

    for col in colunas_converter:
        df[col] = (
            df[col]
            .astype(str).
            str.replace('.', '', regex=False)
            .str.replace(',', '.', regex=False)
        )
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df['deficit_total'] = df['habitacao_precaria'] + df['coabitacao'] + df['onus']
    df.drop(columns=['N', 'deficit_original'], inplace=True)

    df_regioes = df[df['regiao'] != 'Brasil'].copy()
    df_brasil = df[df['regiao'] == 'Brasil'].copy()

    return df_regioes, df_brasil

def dados_limpos_Faixa_De_Renda(df: pd.DataFrame) -> pd.DataFrame:
    df.rename(columns={
    'Regiao' : 'regiao',
    'Faixa de Renda' : 'faixa_de_renda',
    'Domicílios Rústicos' : 'domicilios_rusticos',
    'Domicílios Improvisados' : 'domicilios_improvisados',
    'Habitação Precária' : 'habitacao_precaria',
    'Cômodos' : 'comodos',
    'Unidades conviventes déficit' : 'unidades_conviventes_deficit',
    'Coabitação' : 'coabitacao',
    'Ônus' : 'onus',
    'Déficit Habitacional (Habitação Precária + Coabitação + Ônus)' : 'deficit_original'
    }, inplace=True)

    colunas_excluir = ["regiao", "faixa_de_renda"]

    colunas_converter = [col for col in df.columns if col not in colunas_excluir]

    for col in colunas_converter:
        df[col] = (
            df[col]
            .astype(str).
            str.replace('.', '', regex=False)
            .str.replace(',', '.', regex=False)
        )
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df['onus'] = df['onus'].fillna(0)

    df['deficit_total'] = df['habitacao_precaria'] + df['coabitacao'] + df['onus']
    df.drop(columns=['N', 'deficit_original'], inplace=True)

    df_regioes = df[df['regiao'] != 'Brasil'].copy()
    df_brasil = df[df['regiao'] == 'Brasil'].copy()

    return df_regioes, df_brasil

def dados_limpos_Cor_Raca(df: pd.DataFrame) -> pd.DataFrame:
    df.rename(columns={
    'Regiao' : 'regiao',
    'Cor/Raça' : 'cor_raca',
    'Domicílios Rústicos' : 'domicilios_rusticos',
    'Domicílios Improvisados' : 'domicilios_improvisados',
    'Habitação Precária' : 'habitacao_precaria',
    'Cômodos' : 'comodos',
    'Unidades conviventes déficit' : 'unidades_conviventes_deficit',
    'Coabitação' : 'coabitacao',
    'Ônus' : 'onus',
    'Déficit Habitacional (Habitação Precária + Coabitação + Ônus)' : 'deficit_original'
    }, inplace=True)

    colunas_excluir = ["regiao", "cor_raca", 'N']

    colunas_converter = [col for col in df.columns if col not in colunas_excluir]

    for col in colunas_converter:
        df[col] = (
            df[col]
            .astype(str).
            str.replace('.', '', regex=False)
            .str.replace(',', '.', regex=False)
        )
        df[col] = pd.to_numeric(df[col], errors='coerce')

    if 'N' in df.columns:
        df.rename(columns={'N': 'id_regiao'}, inplace=True)

    df['id_regiao'].fillna(method='ffill', inplace=True)

    df['id_regiao'] = df['id_regiao'].astype(int)

    df['deficit_total'] = df['habitacao_precaria'] + df['coabitacao'] + df['onus']
    df.drop(columns=['id_regiao', 'deficit_original'], inplace=True)

    df_regioes = df[df['regiao'] != 'Brasil'].copy()
    df_brasil = df[df['regiao'] == 'Brasil'].copy()

    return df_regioes, df_brasil