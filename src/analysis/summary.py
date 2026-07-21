import pandas as pd


def duplicate_summary(df: pd.DataFrame) -> None:
    """Exibe informações sobre registros duplicados."""

    print("\n=== DUPLICIDADES ===")
    print(f"Linhas duplicadas: {df.duplicated().sum()}")

    duplicated_wells = df.duplicated(subset=["Poço", "Mês/Ano"]).sum()
    print(f"Poços duplicados no mesmo mês: {duplicated_wells}")