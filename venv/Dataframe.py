import pandas as pd
import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345',
    database='db_tabela'
)

consulta_sql = "SELECT * FROM dados"

df = pd.read_sql(consulta_sql, conexao)

print(df.head())

conexao.close()
