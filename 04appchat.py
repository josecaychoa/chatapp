import streamlit as st
import openai
from PIL import Image
from dotenv import load_dotenv
import os

# ✅ Configura tu API Key de OpenAI
load_dotenv()
openai.api_key = st.secrets["OPEN_API_KEY"]

# Inicializar el historial de chat en el estado de sesión
if "historial" not in st.session_state:
    st.session_state.historial = []

# 📋 Barra lateral
st.sidebar.title("Opciones del Asistente de Viajes")

# 🎚️ Slider para nivel de detalle
detalle = st.sidebar.slider("Nivel de detalle", min_value=1, max_value=10, value=5)

# 🗑️ Botón para borrar historial
if st.sidebar.button("🗑️ Borrar historial"):
    st.session_state.historial = []

# 🧳 Título principal
st.title("🧳 Chat de Viajes con OpenAI-Es 5 pero debe ser 4")

# 📷 Mostrar imagen precargada al iniciar
try:
    imagen_precargada = Image.open("imagen_viaje.jpg")
    st.image(imagen_precargada, caption="Imagen de inspiración para tu viaje", use_container_width=True)
except FileNotFoundError:
    st.warning("No se encontró la imagen 'imagen_viaje.jpg'. Asegúrate de que esté en el mismo directorio que el script.")

# 💬 Entrada de texto
pregunta = st.text_input("¿A dónde te gustaría viajar o qué necesitas planear?")

# 🚀 Botón para enviar
if st.button("Enviar") and pregunta:
    with st.spinner("Consultando al asistente de viajes..."):
        try:
            respuesta = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"Eres un asistente de viajes útil. Responde con nivel de detalle {detalle}/10."},
                    {"role": "user", "content": pregunta}
                ]
            )
            contenido = respuesta.choices[0].message.content
            st.session_state.historial.append(("Tú", pregunta))
            st.session_state.historial.append(("Asistente", contenido))
        except Exception as e:
            st.error(f"Error al conectar con OpenAI: {e}")

# 🗨️ Mostrar historial de conversación
if st.session_state.historial:
    st.markdown("### 🗨️ Historial de conversación")
    for autor, mensaje in st.session_state.historial:
        st.markdown(f"**{autor}:** {mensaje}")


