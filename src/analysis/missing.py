import pandas as pd


def missing_values_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Retorna um resumo dos valores ausentes."""

    summary = pd.DataFrame({
        "Valores Ausentes": df.isna().sum(),
        "Percentual (%)": (df.isna().mean() * 100).round(2)
    })

    return summary.sort_values(
        by="Valores Ausentes",
        ascending=False
    )