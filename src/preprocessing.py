import pandas as pd

def nulos_mediana(df, coluna):
    """
    Substitui valores faltantes pela mediana da coluna.
    
    Parâmetros:
    df (pandas.DataFrame): O DataFrame contendo os dados.
    coluna (str): O nome da coluna na qual os valores faltantes serão substituídos.
    
    Retorna:
    pandas.DataFrame: O DataFrame com os valores faltantes substituídos pela mediana.
    """
    # Calcular a mediana da coluna
    mediana = df[coluna].median()
    
    # Substituir valores NaN pela mediana
    df[coluna].fillna(mediana, inplace=True)
    
    return df