from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/raw/producao-mar-2026.csv")


def load_data() -> pd.DataFrame:
    """Carrega os dados brutos da ANP."""
    return pd.read_csv(
    DATA_PATH,
    sep=",",
    encoding="utf-8"
)