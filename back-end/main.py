from fastapi import FastAPI
import funcao

app = FastAPI(title="Gerenciador de produtos")

@app.get("/")
def home():
    return{"mensagem": "Bem-vindo ao gerenciador de produtos"}

@app.post("/produtos")
def adicionar_produto(nome: str, categoria: str, preco: float, quantidade: float):
    funcao.cadastrar_produto(nome, categoria, preco, quantidade)
    return {"200": "Produto cadastrado com sucessso!"}