from conexao import conector

def criar_tabela():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
        id SERIAL PRIMARY KEY,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade INTEGER  
        )
        """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.commit()

def cadastrar_produto(nome, categoria, preco, quantidade):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
                (nome, categoria, preco, quantidade)
                )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao cadastar o produtos {erro}")
        finally:
            cursor.close()
            conexao.commit()

cadastrar_produto("Placa de Vídeo Galax NVIDIA GeForce RTX 3060", "alta performance", 1.839, 10)