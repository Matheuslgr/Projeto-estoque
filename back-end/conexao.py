import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def conector():
    try:
        conexao = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"), 
            port= os.getenv("DB_PORT")
            )
        cursor = conexao.cursor()
        print("Conexao estabelecida")
        return conexao, cursor
    except Exception as erro:
        print(f"erro de conexao {erro}")
        return None, None
    
conector()
