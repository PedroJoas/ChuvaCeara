import os

import pandas as pd

def junta_caminho(pasta):
    arquivos = ['municipios.csv', 'postos.csv', 'registros.csv']
    caminhos = [os.path.join(pasta, arquivo) for arquivo in arquivos]

    return caminhos


#paths
caminho_bronze = 'data/bronze/csv'
caminho_silver = 'data/silver/csv'

caminho_municipios, caminho_postos, caminho_registros = junta_caminho(caminho_bronze)

# dataframes

municipios = pd.read_csv(caminho_municipios)
postos = pd.read_csv(caminho_postos)
registros = pd.read_csv(caminho_registros)

# Tratamento postos

postos = postos.merge(municipios, on='Municipios')
postos.drop(columns=['Municipios'], inplace=True)

# Tratamento registros

registros = registros[(registros['registros'] != 999) & (registros['registros'] != 888)]
registros = registros.merge(postos[['Postos', 'id_posto']], on='Postos')
registros['id_registro'] = range(1, registros.shape[0] + 1)
registros.dropna(inplace=True)
registros.drop(columns=['Postos'], inplace=True)

# Salvando

os.makedirs(caminho_silver, exist_ok=True)

caminho_municipios_salvo, caminho_postos_salvo, caminho_registros_salvo = junta_caminho(caminho_silver)

municipios.to_csv(caminho_municipios_salvo, index=False)
postos.to_csv(caminho_postos_salvo, index=False)
registros.to_csv(caminho_registros_salvo, index=False)

print('Arquivos salvos na silver!')