import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Análisis Exploratorio",
    layout="wide"
)

st.title("📊 Análisis Exploratorio de Autos Usados")

if 'data' not in st.session_state:
    st.warning("No se han cargado datos aún.")
    st.stop()

data = st.session_state['data']

st.markdown("Explora cómo diferentes variables se relacionan con el precio de reventa.")

numericas = data.select_dtypes(include='number').columns.tolist()
categoricas = data.select_dtypes(include='object').columns.tolist()

chart = st.selectbox("Selecciona el tipo de gráfico", ["Dispersión", "Caja", "Histograma"])

if chart == "Dispersión":
    x = st.selectbox("Eje X:", numericas)
    y = st.selectbox("Eje Y:", numericas, index=1)
    fig = px.scatter(data, x=x, y=y, color_discrete_sequence=['blue'])
    st.plotly_chart(fig)

elif chart == "Caja":
    if categoricas:
        cat = st.selectbox("Categoría:", categoricas)
        val = st.selectbox("Valor numérico:", numericas)
        fig = px.box(data, x=cat, y=val)
        st.plotly_chart(fig)
    else:
        st.warning("No hay columnas categóricas disponibles.")

elif chart == "Histograma":
    col = st.selectbox("Selecciona columna numérica:", numericas)
    fig = px.histogram(data, x=col)
    st.plotly_chart(fig)