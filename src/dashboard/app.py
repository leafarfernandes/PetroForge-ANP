import streamlit as st

from src.data.load import load_data
from src.processing.clean import clean_data
from src.analysis.kpis import production_kpis

# ==========================
# Configuração da página
# ==========================

st.set_page_config(
    page_title="PetroForge",
    page_icon="🛢️",
    layout="wide"
)

st.title("🛢️ PetroForge")
st.subheader("Dashboard da Produção Brasileira de Petróleo (ANP)")

st.divider()

# ==========================
# Carregamento dos dados
# ==========================

df = load_data()
df = clean_data(df)

kpis = production_kpis(df)

# ==========================
# KPIs
# ==========================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Produção Total",
        f"{kpis['oil_total_m3']:,.0f} m³",
    )

with col2:
    st.metric(
        "Poços",
        kpis["wells"],
    )

with col3:
    st.metric(
        "Campos",
        kpis["fields"],
    )

with col4:
    st.metric(
        "Estados",
        kpis["producing_states"],
    )