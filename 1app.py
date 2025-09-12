import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


# 1. Configuración de la página
st.set_page_config(
    page_title="PIB, Desempleo e Inflación",
    layout="wide"
)
st.title("Indicadores Económicos")

@st.cache_data
def load_data():
    
# 2. Cargar y preparar datos
    try:
        # Cargar el archivo CSV y especificar que no use ninguna columna como índice
        df = pd.read_csv("anual.csv", sep=",", index_col=False)
        # Asegurar que la columna 'Fecha' sea de tipo datetime y ordenar los datos
        df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")
        df = df.dropna(subset=["Fecha"]).sort_values("Fecha")
        return df
    except FileNotFoundError:
        st.error("Error")
        return pd.DataFrame()
df = load_data()
# 3. Opciones de visualización en la barra lateral
st.sidebar.header("Opciones de visualización")
st.sidebar.markdown("Elige las series a visualizar:")
variables_seleccionadas = []

# Checkboxes para seleccionar las variables.
if st.sidebar.checkbox("PIB-anual", True):
    variables_seleccionadas.append("PIB")
if st.sidebar.checkbox("Desempleo-anual", True):
    variables_seleccionadas.append("Desempleo")
if st.sidebar.checkbox("Inflación-anual", True):
    variables_seleccionadas.append("Inflacion")

# 4. Generación del gráfico interactivo
if not df.empty and variables_seleccionadas:
    # Crear el gráfico de líneas con Plotly Express
    fig = px.line(
        df,
        x="Fecha",
        y=variables_seleccionadas,
        title="PIB, Desempleo e Inflación",
        markers=True,
        color_discrete_map={
            "PIB": "#A29BFE",
            "Desempleo": "#FAB1A0",
            "Inflacion": "#FD79A8"
        }
    )

    # Actualizar el diseño del gráfico para mejorar la visualización
    fig.update_layout(
        xaxis_title="Fecha",
        yaxis_title="Valor (%)",
        hovermode="x unified",
        legend_title="Indicadores",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        xaxis=dict(
            rangeslider=dict(visible=True),
            type="date"
        )
    )

    # Actualizar el texto que se muestra al pasar el cursor (hover)
    fig.update_traces(
        hovertemplate="Fecha: %{x|%b %Y}<br>Valor: %{y:.2f}%"
    )
    # Mostrar el gráfico en la aplicación Streamlit
    st.plotly_chart(fig, use_container_width=True)

