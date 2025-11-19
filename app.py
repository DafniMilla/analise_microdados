import streamlit as st
import os

st.title("Visualização dos Notebooks")

opcao = st.selectbox(
    "Escolha o notebook:",
    ["Notebook 1", "Notebook 2"]
)

arquivo = "notebooks1.html" if opcao == "Notebook 1" else "notebooks2.html"
caminho = os.path.join("notebooks", arquivo)

if os.path.exists(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        html = f.read()
    st.components.v1.html(html, height=900, scrolling=True)
else:
    st.error(f"Arquivo HTML não encontrado: {caminho}")
