import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Produtos", layout="wide")
st.title("Gerenciador de Produtos")

menu = st.sidebar.radio("Menu",
    ["Estoque Produtos", "Cadastrar Produtos", "Deletar Produtos", "Atualizar Produtos", "Valor Total"]           
     )

if menu == "Estoque Produtos":
    st.subheader("Todos os filmes")
    response = requests.get(f"{API_URL}/produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            st.dataframe(produtos)
        else:
            st.info("Nenhum produto cadastrado ainda ")
    else:
        st.error("Deu erro ao conectar com a API.")

elif menu == "Cadastrar Produtos":
    st.subheader("➕ Adicionar produtos ")
    nome = st.text_input("Titulo do Produto")
    categoria = st.text_input("Categoria do Produto")
    preco = st.number_input("Preço do Produto")
    quantidade = st.number_input("Quantidade do produto", min_value=0, step=1)
    if st.button("Salvar Produto"):
        dados = {"nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade}
        response = requests.post(f"{API_URL}/produtos", params=dados)
        if response.status_code == 200:
            st.success("Produto adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar produto.")

elif menu == "Deletar Produtos":
    st.subheader(" 🗑 Deletar Produtos")
    id_produto = st.number_input("Id do Produto a excluir", min_value=1, step=1)
    if st.button("Excluir"):
        response = requests.delete(f"{API_URL}/produtos/{id_produto}")
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                st.success("Produto excluido  com sucesso!")
            else:
                st.error("Erro ao tentar excluir produto.")
        else:
            st.error("Erro ao excluir o produto")

elif menu == "Atualizar Produtos":
    st.subheader(" Atualizar produto")
    id_produto = st.number_input("Id do produto que deseja atualizar", min_value=1, step=1)
    nova_quantidade = st.number_input("Digite a nova quantidade do Produto", min_value=0,  step=1)
    if st.button("Atualizar"):
        dados = {
            "id_produto": id_produto,
            "nova_quantidade": nova_quantidade
        }
        response = requests.put(f"{API_URL}/produtos/{id_produto}", params=dados)
        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                st.success("Produto atualizado com sucesso!")
            else:
                st.warning(data["erro"])
        else:
            st.error("Erro ao atulizar o produto.")

elif menu == "Valor Total":
    st.subheader("Valor Total do Estoque")
    if st.button("Calcular Valor do estoque"):
        try:
            response = requests.get(f"{API_URL}/valor_total")
            if response.status_code == 200:
                data = response.json()
                valor_total = data["valor_total"]
                st.success(f"O valor total do estoque é: R$ {valor_total}")
            else:
                st.error("Erro ao buscar o valor total do estoque.")
        except Exception as erro:
            st.error(f"Erro ao se conectar com a API:{erro}")
