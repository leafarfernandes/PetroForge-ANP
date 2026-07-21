import pandas as pd


def production_statistics(df: pd.DataFrame) -> dict:
    """Retorna indicadores gerais da produção."""

    oil = df["Produção de Óleo (m³)"]

    stats = {
        "Estados produtores": df.loc[df["Produção de Óleo (m³)"] > 0, "Estado"].dropna().nunique(),
        "Bacias": df["Bacia"].nunique(),
        "Campos": df["Campo"].nunique(),
        "Poços": df["Poço"].nunique(),
        "Registros com produção": oil.notna().sum(),
        "Produção total (m³)": oil.sum(),
        "Produção média por poço (m³)": (
            round(oil.sum() / df["Poço"].nunique(), 2)
        ),
        "Maior produção registrada (m³)": oil.max(),
        "Menor produção registrada (m³)": oil.min(),
    }

    return stats