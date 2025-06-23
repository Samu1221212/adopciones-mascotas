import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Carga de CSV",
    layout="wide"
)

st.title("📥 Cargar Datos de Autos Usados")

required_columns = ['mileage_kmpl', 'engine_cc', 'fuel_type', 'owner_count', 'price_usd']

uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])

if uploaded_file:
    try:
        data = pd.read_csv(uploaded_file)
        data.columns = data.columns.str.strip().str.lower()
        if all(col in data.columns for col in required_columns):
            st.session_state['data'] = data
            st.success("Datos cargados correctamente")
            st.dataframe(data.head())
        else:
            missing = list(set(required_columns) - set(data.columns))
            st.error(f"Faltan columnas requeridas: {missing}")
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
else:
    st.info("Sube un archivo CSV para comenzar")