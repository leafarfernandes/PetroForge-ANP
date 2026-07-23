import pandas as pd


def production_kpis(df: pd.DataFrame) -> dict:
    """Retorna os principais indicadores do projeto."""

    oil = df["Produção de Óleo (m³)"]

    return {
        "oil_total_m3": oil.sum(),
        "oil_average_m3": oil.mean(),
        "oil_maximum_m3": oil.max(),
        "oil_minimum_m3": oil.min(),
        "producing_states": df.loc[
            oil > 0,
            "Estado",
        ].dropna().nunique(),
        "basins": df["Bacia"].nunique(),
        "fields": df["Campo"].nunique(),
        "wells": df["Poço"].nunique(),
    }