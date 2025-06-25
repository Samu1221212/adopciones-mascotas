import streamlit as st
from PIL import Image

# Configuración inicial de la página
st.set_page_config(
    page_title="Centro de Adopción de Mascotas",
    layout="wide",
    page_icon="🐾"
)

# Función principal
def main():
    st.title("🐾 Centro de Análisis de Adopciones")
    st.markdown("---")

    # Sección de bienvenida
    col1, col2 = st.columns([3, 2])

    # Columna izquierda: texto de bienvenida e instrucciones
    with col1:
        st.header("Bienvenido")
        st.write("""
        Este sistema te permite:
        - 📤 **Cargar archivos** de adopciones (CSV/Excel)
        - 📊 **Visualizar y explorar** datos de mascotas y adoptantes
        - 📈 **Realizar análisis** exploratorio con gráficos interactivos
        - 🤖 **Predecir adopciones** usando Machine Learning
        - 🎯 **Obtener insights** para mejorar las tasas de adopción
        """)

        st.info("💡 **Pasos para usar el sistema:**")
        st.markdown("""
        1. Ve a **📤 Inicio** para cargar tu archivo de datos  
        2. Explora los datos en **📊 Análisis Exploratorio**  
        3. Usa **🤖 Machine Learning** para entrenar modelos y hacer predicciones
        """)

        # Estadísticas si los datos están cargados
        if 'data' in st.session_state:
            data = st.session_state['data']
            st.success("✅ Datos cargados correctamente")

            col_stats1, col_stats2, col_stats3 = st.columns(3)

            with col_stats1:
                st.metric("🐶 Total Mascotas", len(data))

            with col_stats2:
                if 'Adoptado' in data.columns:
                    total_adoptadas = data['Adoptado'].sum()
                    st.metric("🏠 Adoptadas", int(total_adoptadas))

            with col_stats3:
                if 'Adoptado' in data.columns:
                    tasa = (data['Adoptado'].sum() / len(data)) * 100
                    st.metric("📈 Tasa de Adopción", f"{tasa:.1f}%")

    # Columna derecha: imagen e información del sistema
    with col2:
        st.image(
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ3GceXOZTF7Ia18e-VD5qWTtUVsYQ7rO4gWg&s",
            caption="Adopta una mascota 🐶🐱🐰"
        )

        st.markdown("### 🔧 Características del Sistema")
        st.markdown("""
        - **Algoritmos ML**: Random Forest, Regresión Logística, SVM  
        - **Visualizaciones**: Interactivas con Plotly  
        - **Métricas**: Precisión, matriz de confusión, importancia de características  
        - **Predicciones**: En tiempo real para nuevas mascotas  
        """)

# Ejecutar aplicación
if __name__ == "__main__":
    main()

# Línea de separación final
st.markdown("---")

# Pie de página
st.caption("Proyecto desarrollado con Streamlit, Plotly y scikit-learn | © 2025 Big Data")
