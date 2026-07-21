import pandas as pd

def oil_production_by(
    df: pd.DataFrame,
    group_by: str,
    top_n: int | None = None,
) -> pd.DataFrame:
    """Retorna a produção e a participação percentual por categoria."""

    oil_column = "Produção de Óleo (m³)"

    production = (
        df.groupby(group_by, dropna=False)[oil_column]
        .sum(min_count=1)
        .reset_index()
        .sort_values(oil_column, ascending=False)
        .reset_index(drop=True)
    )

    total = production[oil_column].sum(min_count=1)

    if pd.isna(total) or total == 0:
        production["Participação (%)"] = pd.NA
    else:
        production["Participação (%)"] = (
            production[oil_column]
            .div(total)
            .mul(100)
            .round(2)
        )

    if top_n is not None:
        production = production.head(top_n).copy()

    return production.reset_index(drop=True)

def oil_production_by_month(df: pd.DataFrame) -> pd.DataFrame:
    production = (
        df.groupby("Mês/Ano")["Produção de Óleo (m³)"]
        .sum()
        .reset_index()
        .sort_values("Mês/Ano")
    )

    production["Variação (%)"] = (
        production["Produção de Óleo (m³)"]
        .pct_change() * 100
    )

    production["Variação (%)"] = production["Variação (%)"].round(2)

    return production

def oil_production_by_state(df):
    return oil_production_by(df, "Estado")


def oil_production_by_basin(df):
    return oil_production_by(df, "Bacia")


def oil_production_by_field(df, top_n=10):
    return oil_production_by(df, "Campo", top_n)