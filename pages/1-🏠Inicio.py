import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Inicio",
    layout="wide"
)

st.title("📤 Cargar Archivo de Adopciones")

@st.cache_data
def load_data(file):
    if file.name.endswith('.csv'):
        data = pd.read_csv(file)
    elif file.name.endswith('.xlsx'):
        data = pd.read_excel(file)
    else:
        st.error("Formato no soportado")
        return None

    # Eliminar duplicados
    data = data.drop_duplicates()

    # Renombrar columnas al español para visualización
    columnas = {
        "pet_id": "ID Mascota",
        "pet_name": "Nombre",
        "species": "Especie",
        "breed": "Raza",
        "age_years": "Edad (años)",
        "gender": "Género",
        "color": "Color",
        "arrival_date": "Fecha de llegada",
        "adopted": "Adoptado",
        "adoption_date": "Fecha de adopción",
        "adopter_id": "ID Adoptante",
        "adopter_name": "Nombre Adoptante",
        "adopter_age": "Edad Adoptante",
        "adopter_city": "Ciudad",
        "adopter_previous_pets": "Mascotas previas"
    }
    data.rename(columns=columnas, inplace=True)

    # Filtrar filas donde falten los campos necesarios para el modelo
    campos_modelo = ["Especie", "Raza", "Edad (años)", "Color", "Adoptado"]
    data = data.dropna(subset=campos_modelo)

    return data

uploaded_file = st.file_uploader("Sube tu archivo CSV", type=["csv"])

if uploaded_file:
    data = load_data(uploaded_file)
    if data is not None:
        st.session_state['data'] = data
        st.success("¡Archivo cargado y limpiado correctamente!")
        st.dataframe(data.head())
else:
    st.info("Por favor, sube un archivo para comenzar.")