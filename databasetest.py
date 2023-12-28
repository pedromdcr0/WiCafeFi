import sqlite3
import pandas as pd

# Substitua 'seuarquivo.db' pelo nome do seu arquivo .db
nome_arquivo_db = 'models/cafes.db'

# Conectar ao banco de dados
conexao = sqlite3.connect(nome_arquivo_db)

# Criar um cursor para executar consultas SQL
cursor = conexao.cursor()

# Exemplo: executar uma consulta para selecionar todos os dados da tabela 'cafe'
cursor.execute('SELECT * FROM cafe')

# Recuperar todos os resultados da consulta
resultados = cursor.fetchall()

# Obter os nomes das colunas
nomes_colunas = [descricao[0] for descricao in cursor.description]

# Criar um DataFrame Pandas
df = pd.DataFrame(resultados, columns=nomes_colunas)

# Exibir todas as colunas do DataFrame
pd.set_option('display.max_columns', None)
print(df)

# Fechar a conexão
conexao.close()
