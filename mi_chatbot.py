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
user_input = # Pedimos al usuario que escriba un mensaje
user_input = st.text_input("Escribe tu mensaje:")

# Si el usuario escribe algo
if user_input:
    # Guardamos el mensaje en el historial de la sesión
    st.session_state.historial.append({"role": "user", "content": user_input})
if user_input:
    mensajes.append({"role": "user", "content": user_input})# Llamada a OpenAI usando todo el historial
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": "Eres un asistente divertido y amigable."}] + st.session_state.historial,
    temperature=0.7
)

# Guardar la respuesta de la IA en el historial
st.session_state.historial.append({"role": "assistant", "content": response['choices'][0]['message']['content']})

    
    # Paso 3: llamar a OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=mensajes,
        temperature=0.7
    )
    st.write(response['choices'][0]['message']['content']) 
# Pega aquí TODO el código de Streamlit que escribiste arriba# Mostrar todo el historial en burbujas de chat
for mensaje in st.session_state.historial:
    if mensaje["role"] == "user":
        st.chat_message("user").write(mensaje["content"])
    else:
        st.chat_message("assistant").write(mensaje["content"])
