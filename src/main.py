from data.load import load_data
from analysis.statistics import production_statistics
from utils.logger import get_logger
from processing.clean import clean_data
from visualization.plots import (
    plot_monthly_oil_production,
    plot_oil_by_state,
    plot_oil_by_field,
    plot_oil_by_basin,
    plot_oil_by_well,
    plot_oil_vs_gas,
    plot_heatmap_state_month,
    plot_treemap_oil
)
from analysis.production import (
    oil_production_by_state,
    oil_production_by_basin,
    oil_production_by_field,
    oil_production_by_month,
    oil_production_by_well,
    oil_gas_by_month,
    oil_heatmap_state_month,
    oil_production_treemap
)

logger = get_logger(__name__)

df = load_data()
df = clean_data(df)

states = oil_production_by_state(df)
basins = oil_production_by_basin(df)
fields = oil_production_by_field(df)
monthly = oil_production_by_month(df)
wells = oil_production_by_well(df)
oil_gas = oil_gas_by_month(df)
heatmap = oil_heatmap_state_month(df)
treemap = oil_production_treemap(df)

print(states)
print()
print(basins)
print()
print(fields)
print()
print(monthly)

logger.info("=== INDICADORES GERAIS ===")

stats = production_statistics(df)

plot_monthly_oil_production(monthly).show()

plot_oil_by_state(states).show()

plot_oil_by_basin(basins).show()

plot_oil_by_field(fields).show()

plot_oil_by_well(wells).show()

plot_oil_vs_gas(oil_gas).show()

plot_heatmap_state_month(heatmap).show()

plot_treemap_oil(treemap).show()

for indicador, valor in stats.items():
    logger.info(f"{indicador}: {valor}")