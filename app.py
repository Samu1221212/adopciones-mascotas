import streamlit as st

st.set_page_config(
    page_title="Estimador de Precio de Autos Usados",
    layout="wide",
    page_icon="🚗"
)

def main():
    st.title("🚗 Estimador de Precio de Autos Usados")
    st.markdown("---")

    col1, col2 = st.columns([3, 2])

    with col1:
        st.header("Bienvenido")
        st.write("""
        Esta aplicación te permite:
        - Cargar un archivo CSV con información de autos usados
        - Analizar variables como kilometraje, motor, tipo de combustible
        - Visualizar relaciones entre variables
        - Predecir el precio de reventa de los vehículos
        """)
        st.info("💡 Comienza subiendo tu archivo en el menú lateral")

    with col2:
        st.image("https://cdn.pixabay.com/photo/2016/10/12/13/34/car-1736072_960_720.jpg")

if __name__ == "__main__":
    main()