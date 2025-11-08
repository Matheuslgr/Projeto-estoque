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


@app.get("/produtos")
def listar_produtos():
    produtos = funcao.listar_produto()
    lista = []
    for linha in produtos:
        lista.append(
            { 
                "id": linha[0],
                "nome": linha[1],
                "categoria": linha[2],
                "preco": linha[3],
                "quantidade": linha[4]
            }
        )
    return{"produtos": lista}

@app.delete("/produtos/{id}")
def deletar_produto(id: int):
    produtos = funcao.buscar_produto(id)
    if produtos:
        funcao.remover_produto(id)
        return{"200": "Produto excluido com sucesso!"}
    else:
        return{"erro": "filme não encontrado"}