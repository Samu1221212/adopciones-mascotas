import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Análisis Exploratorio",
    layout="wide"
)

st.title("📊 Análisis de Datos de Adopción")

if 'data' not in st.session_state:
    st.warning("Primero debes cargar los datos en la página de inicio.")
    st.stop()

data = st.session_state['data']

st.subheader("Vista previa de los datos")
st.dataframe(data.head())

st.markdown("---")

# Histogramas
st.subheader("Distribuciones por variable")
columnas_numericas = data.select_dtypes(include='number').columns.tolist()
if columnas_numericas:
    col = st.selectbox("Selecciona una variable numérica para ver su distribución:", columnas_numericas)
    fig = px.histogram(data, x=col, title=f"Distribución de {col}", color_discrete_sequence=['indianred'])
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de barras - CORREGIDO
st.subheader("Conteo de valores por categoría")
columnas_categoricas = data.select_dtypes(include='object').columns.tolist()
if columnas_categoricas:
    col_cat = st.selectbox("Selecciona una variable categórica:", columnas_categoricas)
    # Corrección: Crear el DataFrame de conteos correctamente
    conteos_df = data[col_cat].value_counts().reset_index()
    conteos_df.columns = [col_cat, 'Cantidad']
    fig2 = px.bar(conteos_df, x=col_cat, y='Cantidad', 
                  title=f"Frecuencia por {col_cat}",
                  color_discrete_sequence=['steelblue'])
    st.plotly_chart(fig2, use_container_width=True)

# Mapa de calor de correlación
st.subheader("Mapa de calor de correlación")
if len(columnas_numericas) >= 2:
    corr = data[columnas_numericas].corr()
    fig3, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap='Blues', ax=ax)
    st.pyplot(fig3)

# Boxplot
st.subheader("Distribución por categorías (Boxplot)")
if columnas_categoricas and columnas_numericas:  # Añadida verificación adicional
    cat_for_box = st.selectbox("Selecciona categoría para comparar:", columnas_categoricas)
    num_for_box = st.selectbox("Selecciona variable numérica:", columnas_numericas)
    fig4 = px.box(data, x=cat_for_box, y=num_for_box, title=f"{num_for_box} por {cat_for_box}")
    st.plotly_chart(fig4, use_container_width=True)