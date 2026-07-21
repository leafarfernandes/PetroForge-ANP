from data.load import load_data
from analysis.statistics import production_statistics
from processing.clean import clean_data
from analysis.production import (
    oil_production_by_state,
    oil_production_by_basin,
    oil_production_by_field,
    oil_production_by_month,
)

df = load_data()
df = clean_data(df)

print(oil_production_by_state(df))
print()
print(oil_production_by_basin(df))
print()
print(oil_production_by_field(df))
print()
print(oil_production_by_month(df))

print("\n=== INDICADORES GERAIS ===")

stats = production_statistics(df)

for indicador, valor in stats.items():
    print(f"{indicador}: {valor}")