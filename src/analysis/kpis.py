import pandas as pd


def production_kpis(df: pd.DataFrame) -> dict:
    """
    Retorna os principais indicadores do projeto.
    """

    oil = df["Produção de Óleo (m³)"]

    return {
        "Produção Total (m³)": oil.sum(),
        "Produção Média (m³)": oil.mean(),
        "Produção Máxima (m³)": oil.max(),
        "Produção Mínima (m³)": oil.min(),
        "Estados Produtores": df.loc[
            oil > 0, "Estado"
        ].dropna().nunique(),
        "Bacias": df["Bacia"].nunique(),
        "Campos": df["Campo"].nunique(),
        "Poços": df["Poço"].nunique(),
    }