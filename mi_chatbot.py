import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Mi Chatbot IA", page_icon="🤖")

st.title("💬 Mi Chatbot IA")

if "historial" not in st.session_state:
    st.session_state.historial = []

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Mostrar el historial
for mensaje in st.session_state.historial:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["content"])

# Entrada del usuario
if prompt := st.chat_input("Escribe un mensaje..."):
    st.session_state.historial.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Llamada al modelo de OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un asistente divertido y amigable."},
            *st.session_state.historial,
        ],
        temperature=0.7,
    )

    respuesta = response.choices[0].message.content

    with st.chat_message("assistant"):
        st.markdown(respuesta)

    st.session_state.historial.append({"role": "assistant", "content": respuesta})
