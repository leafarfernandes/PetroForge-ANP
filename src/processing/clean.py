import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Padroniza os nomes das colunas."""

    df.columns = (
        df.columns
        .str.replace("[", "", regex=False)
        .str.replace("]", "", regex=False)
        .str.strip()
    )

    return df


def convert_date_column(df: pd.DataFrame) -> pd.DataFrame:
    """Converte a coluna Mês/Ano para datetime."""

    df["Mês/Ano"] = pd.to_datetime(
        df["Mês/Ano"],
        format="%m/%Y",
    )

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Executa todas as etapas de limpeza dos dados."""

    df = clean_column_names(df)
    df = convert_date_column(df)

    return df