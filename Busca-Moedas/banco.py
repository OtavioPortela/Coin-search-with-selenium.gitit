import sqlite3
from datetime import date

conexao = sqlite3.connect('paises.db3')
cursor = conexao.cursor()

def criar_tabela():
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS tb_paises(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       Pais VARCHAR(50),
                       Valor_em_Real VARCHAR(10),
                       Data VARCHAR(10)
                   )
                   """)
    conexao.commit()
    return 'Tabela criada com sucesso!!'

def inserir_pais(pais, valor):
    cursor.execute('''
                  
                   INSERT INTO tb_paises(Pais, Valor_em_Real, Data)
                   VALUES (?, ?, ?)
                   ''', (pais, valor, date.today()))
    conexao.commit()
    return f'{pais} adicionado com sucesso !!'

def deleta_pais(id):
    cursor.execute("""
            DELETE FROM tb_paises
            WHERE id = ?
        """, (id,))
    conexao.commit()
    return 'Pais deletado da tabela'
    
def visualizar_todos():
    paises = cursor.execute("""
                   SELECT * FROM tb_paises
                   """)
    conexao.commit()
    lista = [x for x in paises]
    return lista