from fastapi import FastAPI
import funcao

app = FastAPI(title="Gerenciador de produtos")

@app.get("/")
def home():
    return{"mensagem": "Bem-vindo ao gerenciador de produtos"}