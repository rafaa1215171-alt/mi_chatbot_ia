import streamlit as st
import openai

# Configuración de la página
st.set_page_config(
    page_title="Mi Chatbot IA",
    page_icon="💬",
    layout="wide"
)

# Tu API Key de OpenAI
openai.api_key = "TU_API_KEY"  # <- reemplaza esto con tu API Key

# Crear historial si no existe
if "historial" not in st.session_state:
    st.session_state.historial = []

# Título de la app
st.title("💬 Mi Chatbot IA")

# Caja de texto para el usuario
st.markdown("💬 **Escribe aquí tu mensaje:**")
user_input = st.text_input("", key="entrada_usuario")

# Si el usuario escribe algo
if user_input:
    # Guardar mensaje del usuario
    st.session_state.historial.append({"role": "user", "content": user_input})

    # Llamar a OpenAI con todo el historial
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Eres un asistente divertido y amigable."}] + st.session_state.historial,
        temperature=0.7
    )

    # Guardar respuesta de la IA
    st.session_state.historial.append({"role": "assistant", "content": response['choices'][0]['message']['content']})

# Mostrar solo los últimos 20 mensajes en burbujas estilo chat
for mensaje in st.session_state.historial[-20:]:
    if mensaje["role"] == "user":
        st.chat_message("user").write(mensaje["content"])
    else:
        st.chat_message("assistant").write(mensaje["content"])
