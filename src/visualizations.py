# Funções de visualização customizadas

import matplotlib.pyplot as plt
import seaborn as sns

def grafico_barras(df, coluna_x, coluna_y, titulo=""):
    plt.figure(figsize=(12,6))
    sns.barplot(x=coluna_x, y=coluna_y, data=df)
    plt.title(titulo)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
