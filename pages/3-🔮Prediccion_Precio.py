import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Predicción de Precio",
    layout="wide"
)

st.title("🔮 Predicción del Precio de Reventa")

if 'data' not in st.session_state:
    st.warning("Carga primero un archivo CSV válido.")
    st.stop()

data = st.session_state['data']

st.markdown("Selecciona una característica numérica para predecir el precio del vehículo.")

numericas = data.select_dtypes(include='number').columns.tolist()

if 'price_usd' not in numericas:
    st.error("La columna 'price' no está disponible.")
    st.stop()

X_cols = [col for col in numericas if col != 'price']

feature = st.selectbox("Variable independiente (X):", X_cols)

if st.button("Entrenar modelo"):
    X = data[[feature]].dropna()
    y = data['price_usd'].loc[X.index]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    st.success("Modelo entrenado con éxito")
    st.write(f"Coeficiente: {model.coef_[0]:.2f}")
    st.write(f"Intercepto: {model.intercept_:.2f}")
    st.write(f"R²: {r2_score(y_test, y_pred):.2f}")

    fig, ax = plt.subplots()
    ax.scatter(X_test, y_test, label="Real")
    ax.plot(X_test, y_pred, color='red', label="Predicción")
    ax.set_xlabel(feature)
    ax.set_ylabel("price_usd")
    ax.legend()
    st.pyplot(fig)