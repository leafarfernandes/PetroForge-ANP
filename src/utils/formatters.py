def format_volume(value: float) -> str:
    """
    Formata volumes de produção.
    """

    if value >= 1_000_000:
        return f"{value / 1_000_000:.2f} milhões m³"

    if value >= 1_000:
        return f"{value / 1_000:.2f} mil m³"

    return f"{value:.2f} m³"


def format_integer(value: int) -> str:
    """
    Formata números inteiros com separador de milhar.
    """

    return f"{value:,}".replace(",", ".")