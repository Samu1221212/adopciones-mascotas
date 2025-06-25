import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="Predicción Adopción", page_icon="🐾", layout="wide")
st.title("🐾 Predicción de Adopción según Características del Animal")

# 📥 Verificar que los datos están cargados
if 'data' not in st.session_state:
    st.warning("Primero debes cargar los datos desde la página de inicio.")
    st.stop()

# Cargar datos originales
df = st.session_state['data'].copy()

# 🔍 Detección automática de columnas necesarias
columnas_requeridas = {
    'especie': ['especie', 'species', 'tipo', 'animal'],
    'raza': ['raza', 'breed'],
    'edad': ['edad', 'age', 'años', 'year'],
    'color': ['color', 'pelaje'],
    'adoptado': ['adoptado', 'adopted', 'estado']
}

def detectar_columna(posibles_nombres, columnas_df):
    for palabra in posibles_nombres:
        for col in columnas_df:
            if palabra.lower() in col.lower().replace(" ", "").replace("_", ""):
                return col
    return None

col_map = {}
for key, opciones in columnas_requeridas.items():
    encontrada = detectar_columna(opciones, df.columns)
    if encontrada:
        col_map[key] = encontrada

faltantes = [k for k in columnas_requeridas if k not in col_map]
if faltantes:
    st.error(f"⚠️ Faltan columnas necesarias: {faltantes}")
    st.stop()

# 🧼 Limpiar datos
df = df[list(col_map.values())].dropna()
df = df[df[col_map['edad']] >= 0]

# 🧠 Guardar columnas originales
col_especie = col_map['especie']
col_raza = col_map['raza']
col_color = col_map['color']
col_edad = col_map['edad']
col_adoptado = col_map['adoptado']

# 🏷️ Codificar categorías
le_especie = LabelEncoder()
le_raza = LabelEncoder()
le_color = LabelEncoder()

df[col_especie] = le_especie.fit_transform(df[col_especie].astype(str))
df[col_raza] = le_raza.fit_transform(df[col_raza].astype(str))
df[col_color] = le_color.fit_transform(df[col_color].astype(str))
df[col_adoptado] = df[col_adoptado].astype(int)

# 🧠 Entrenar modelo
X = df[[col_especie, col_raza, col_edad, col_color]]
y = df[col_adoptado]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# 📈 Evaluación del modelo
st.subheader("📊 Evaluación del Modelo")
col1, col2 = st.columns(2)
col1.metric("Precisión", f"{accuracy_score(y_test, modelo.predict(X_test)):.2%}")
col2.metric("Total de muestras", len(df))

# 🎯 PREDICCIÓN PERSONALIZADA CON FILTRO POR ESPECIE
st.markdown("---")
st.subheader("🎯 Predicción Personalizada")

# Volver a usar datos sin codificar para interfaz
df_ui = st.session_state['data'].copy().dropna()

# Opciones de especie únicas
especies = sorted(df_ui[col_map['especie']].unique())
especie_input = st.selectbox("🐾 Especie", especies)

# Filtrar solo registros de esa especie
df_filtrado = df_ui[df_ui[col_map['especie']] == especie_input]

# Opciones de raza y color válidas para esa especie
razas_validas = sorted(df_filtrado[col_map['raza']].dropna().unique())
colores_validos = sorted(df_filtrado[col_map['color']].dropna().unique())

# Mostrar selección dependiente
raza_input = st.selectbox("🏷️ Raza", razas_validas)
color_input = st.selectbox("🎨 Color", colores_validos)
edad_min = int(df_ui[col_map['edad']].min())
edad_max = int(df_ui[col_map['edad']].max())
edad_input = st.slider("🎂 Edad (años)", edad_min, edad_max, step=1)

# Botón de predicción
if st.button("🔮 Predecir adopción"):
    try:
        especie_cod = le_especie.transform([especie_input])[0]
        raza_cod = le_raza.transform([raza_input])[0]
        color_cod = le_color.transform([color_input])[0]

        datos_pred = pd.DataFrame([{
            col_especie: especie_cod,
            col_raza: raza_cod,
            col_edad: edad_input,
            col_color: color_cod
        }])

        pred = modelo.predict(datos_pred)[0]
        prob = modelo.predict_proba(datos_pred)[0][1]

        if pred == 1:
            st.success(f"✅ Alta probabilidad de adopción ({prob:.2%})")
        else:
            st.warning(f"⚠️ Baja probabilidad de adopción ({prob:.2%})")

    except Exception as e:
        st.error(f"❌ Error al predecir: {e}")

st.caption("🐶 Sistema mejorado de predicción con selección inteligente por especie")