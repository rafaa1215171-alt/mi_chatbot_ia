import streamlit as st
import openai
import os  # Para leer la API Key desde Secrets

# Configuración de la página
st.set_page_config(
    page_title="Mi Chatbot IA",
    page_icon="💬",
    layout="wide"
)

# Leer API Key desde Secrets
openai.api_key = os.environ["OPENAI_API_KEY"]

# Crear historial si no existe
if "historial" not in st.session_state:
    st.session_state.historial = []

# Título de la app
st.title("💬 Mi Chatbot IA")

# Caja de texto para que el usuario escriba
user_input = st.text_input("Escribe tu mensaje aquí:", key="entrada_usuario")

if user_input:
    # Guardar el mensaje del usuario
    st.session_state.historial.append({"role": "user", "content": user_input})

    # Llamar a OpenAI para obtener la respuesta
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Eres un asistente divertido y amigable."}] + st.session_state.historial,
        temperature=0.7
    )

    # Guardar la respuesta de la IA
    st.session_state.historial.append({
        "role": "assistant",
        "content": response['choices'][0]['message']['content']
    })

# Mostrar los últimos 20 mensajes en estilo
