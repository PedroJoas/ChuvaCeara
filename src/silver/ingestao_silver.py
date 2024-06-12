import os
import psycopg2
import json

# Arquivos csv
caminho_data_silver = 'data/silver/csv'
arquivos_data_silver = sorted([os.path.join(caminho_data_silver, file) for file in os.listdir(caminho_data_silver) if file.endswith('.csv')])

# parâmetros para conectar no db
with open('database/config.json', 'r') as f:
    params = json.load(f)

# Conexão e cursor
conn = psycopg2.connect(**params)

cur = conn.cursor()

# Recuperando nome das tabelas do db
query = """
SELECT tablename 
FROM pg_tables 
WHERE schemaname = 'public';
"""

# Executar a consulta
cur.execute(query)

# Obter os resultados
tables = sorted([table[0] for table in cur.fetchall()])

arquivo_tables = list(zip(tables, arquivos_data_silver))

for table, arquivo  in arquivo_tables:
    with open(arquivo) as f:

        colunas = tuple(f.readline().lower().strip().split(',')) # Pegando primeira linha que contém as colunas do arquivo
        cur.copy_from(f, table, sep=',', columns=colunas)

        print(f"Dados inseridos na tabela {table} a partir do arquivo {arquivo}")

conn.commit()
cur.close()
conn.close()
