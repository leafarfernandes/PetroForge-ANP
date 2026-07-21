import pandas as pd

def oil_production_by(df: pd.DataFrame, group_by: str, top_n: int | None = None) -> pd.DataFrame:
    production = (
        df.groupby(group_by)["Produção de Óleo (m³)"]
        .sum()
        .reset_index()
        .sort_values("Produção de Óleo (m³)", ascending=False)
    )

    if top_n is not None:
        production = production.head(top_n)

    total = production["Produção de Óleo (m³)"].sum()

    production["Participação (%)"] = (
        production["Produção de Óleo (m³)"] / total * 100
    ).round(2)

    return production

def oil_production_by_state(df):
    return oil_production_by(df, "Estado")


def oil_production_by_basin(df):
    return oil_production_by(df, "Bacia")


def oil_production_by_field(df, top_n=10):
    return oil_production_by(df, "Campo", top_n)