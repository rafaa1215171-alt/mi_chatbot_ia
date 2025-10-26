import streamlit as st
import openai# Guardar todos los mensajes en la sesión
if "historial" not in st.session_state:
    st.session_state.historial = []

openai.api_key = "TU_API_KEY"

# --- Aquí empieza la conversación ---
# Paso 1: mensaje inicial de personalidad
mensajes = [
    {
        "role": "system",
        "content": "Eres un asistente divertido y amigable que responde con humor y claridad."
    }
]

# Paso 2: mensaje del usuario
user_input = st.text_input("Escribe tu mensaje:")
if user_input:
    mensajes.append({"role": "user", "content": user_input})
    
    # Paso 3: llamar a OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=mensajes,
        temperature=0.7
    )
    st.write(response['choices'][0]['message']['content']) 
# Pega aquí TODO el código de Streamlit que escribiste arriba
