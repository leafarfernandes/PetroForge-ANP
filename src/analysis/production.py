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

def oil_production_by_well(df, top_n=15):
    """
    Retorna os poços com maior produção de óleo.
    """

    production = (
        df.groupby("Poço", dropna=False)["Produção de Óleo (m³)"]
        .sum(min_count=1)
        .sort_values(ascending=False)
    )

    total = production.sum()

    production = production.reset_index()

    production["Participação (%)"] = (
        production["Produção de Óleo (m³)"] / total * 100
    )

    return production.head(top_n)

def oil_gas_by_month(df):
    """
    Produção mensal de óleo e gás.
    """

    production = (
        df.groupby("Mês/Ano")[
            [
                "Produção de Óleo (m³)",
                "Produção de Gás Associado (Mm³)",
                "Produção de Gás Não Associado (Mm³)"
            ]
        ]
        .sum(min_count=1)
        .reset_index()
        .sort_values("Mês/Ano")
    )

    production["Produção Total de Gás (Mm³)"] = (
        production["Produção de Gás Associado (Mm³)"].fillna(0)
        + production["Produção de Gás Não Associado (Mm³)"].fillna(0)
    )

    return production

def oil_heatmap_state_month(df):
    """
    Produção de óleo por Estado e Mês.
    """

    heatmap = (
        df.groupby(
            ["Estado", "Mês/Ano"],
            dropna=False
        )["Produção de Óleo (m³)"]
        .sum(min_count=1)
        .reset_index()
    )

    heatmap = heatmap.pivot(
        index="Estado",
        columns="Mês/Ano",
        values="Produção de Óleo (m³)"
    )

    return heatmap

def oil_production_treemap(df):

    treemap = (
        df.groupby(
            ["Estado", "Campo"],
            dropna=False
        )["Produção de Óleo (m³)"]
        .sum(min_count=1)
        .reset_index()
    )

    treemap = treemap.dropna(subset=["Estado", "Campo"])

    return treemap

def oil_production_by_state(df):
    return oil_production_by(df, "Estado")


def oil_production_by_basin(df):
    return oil_production_by(df, "Bacia")


def oil_production_by_field(df, top_n=10):
    return oil_production_by(df, "Campo", top_n)