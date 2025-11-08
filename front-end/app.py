import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Produtos", layout="wide")
st.title("Gerenciador de Produtos")

menu = st.sidebar.radio("Menu",
    ["Catálogo Produtos", "Cadastrar Produtos", "Deletar Produtos", "Atualizar Produtos"] 
                        
                        
                        )