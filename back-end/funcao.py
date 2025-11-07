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

def listar_produto():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produtos ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar os produtos {erro}")
            return []
        finally:
            cursor.close()
            conexao.commit()

def atualizar_produto(id, nova_quantidade):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "UPDATE produtos SET quantidade = %s WHERE id = %s",
                (nova_quantidade, id)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar ao atualizar o produto {erro}")
        finally:
            cursor.close()
            conexao.commit()
atualizar_produto(1, 5)