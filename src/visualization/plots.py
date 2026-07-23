import plotly.express as px

def plot_monthly_oil_production(monthly_df):
    """
    Gráfico da produção mensal de óleo.
    """

    fig = px.line(
        monthly_df,
        x="Mês/Ano",
        y="Produção de Óleo (m³)",
        markers=True,
        title="Produção Mensal de Óleo"
    )

    fig.update_layout(
        xaxis_title="Mês",
        yaxis_title="Produção (m³)",
        template="plotly_white"
    )

    return fig

def plot_oil_by_state(states_df):
    """
    Gráfico da produção de óleo por estado.
    """

    fig = px.bar(
        states_df,
        x="Produção de Óleo (m³)",
        y="Estado",
        orientation="h",
        title="Produção de Óleo por Estado",
        text="Produção de Óleo (m³)"
    )

    fig.update_layout(
        xaxis_title="Produção (m³)",
        yaxis_title="",
        template="plotly_white"
    )

    fig.update_traces(texttemplate="%{text:,.0f}", textposition="outside")

    return fig

import plotly.express as px


def plot_oil_by_field(field_df):
    """
    Top campos produtores de óleo.
    """

    fig = px.bar(
        field_df,
        x="Produção de Óleo (m³)",
        y="Campo",
        orientation="h",
        title="Top 10 Campos Produtores",
        text="Participação (%)"
    )

    fig.update_layout(
        template="plotly_white",
        yaxis={"categoryorder": "total ascending"},
        xaxis_title="Produção de Óleo (m³)",
        yaxis_title="Campo"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    return fig

def plot_oil_by_basin(basin_df):
    """
    Gráfico dos principais produtores por bacia.
    """

    fig = px.bar(
        basin_df,
        x="Produção de Óleo (m³)",
        y="Bacia",
        orientation="h",
        title="Produção de Óleo por Bacia",
        text="Participação (%)"
    )

    fig.update_layout(
        template="plotly_white",
        yaxis=dict(categoryorder="total ascending")
    )

    fig.update_traces(texttemplate="%{text:.2f}%", textposition="outside")

    return fig

def plot_oil_by_well(well_df):
    """
    Top 15 poços produtores.
    """

    fig = px.bar(
        well_df,
        x="Produção de Óleo (m³)",
        y="Poço",
        orientation="h",
        text="Participação (%)",
        title="Top 15 Poços Produtores"
    )

    fig.update_layout(
        template="plotly_white",
        yaxis=dict(categoryorder="total ascending")
    )

    fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    return fig

def plot_oil_vs_gas(monthly_df):
    """
    Comparação entre produção mensal de óleo e gás.
    """

    fig = px.line(
        monthly_df,
        x="Mês/Ano",
        y=[
            "Produção de Óleo (m³)",
            "Produção Total de Gás (Mm³)"
        ],
        markers=True,
        title="Produção Mensal de Óleo x Gás"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_title="Mês"
    )

    return fig

def plot_heatmap_state_month(heatmap_df):
    """
    Heatmap da produção por Estado e mês.
    """

    fig = px.imshow(
        heatmap_df,
        aspect="auto",
        text_auto=".2s",
        title="Produção de Óleo por Estado e Mês",
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        template="plotly_white"
    )

    return fig

def plot_treemap_oil(treemap_df):
    """
    Treemap da produção de óleo.
    """

    fig = px.treemap(
        treemap_df,
        path=["Estado", "Campo"],
        values="Produção de Óleo (m³)",
        color="Produção de Óleo (m³)",
        color_continuous_scale="Blues",
        title="Produção de Óleo por Estado e Campo"
    )

    fig.update_layout(
        template="plotly_white"
    )

    return fig