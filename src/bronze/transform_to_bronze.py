import pandas as pd
import os
import re
from datetime import datetime
from tqdm import tqdm

class Tranformador_raw():

    dir_data_raw = 'data/raw/txt'

    def __init__(self, dir_data_bronze):
        self.dir_data_bronze = dir_data_bronze

    def TrataDados(self):
        df = self._monta_df_raw()
        try:
            self._df_registros(df)
            self._df_municipios(df)
            self._df_postos(df)

            print('Arquivos montados com sucesso!')
        except Exception as e:
            print(f'Falha ao montar os arquivos. {e}')

    def _monta_df_raw(self):
        dfs = [pd.read_csv(os.path.join(self.dir_data_raw, file), sep=';') for file in os.listdir(self.dir_data_raw) if file.endswith('.txt')]
        df = pd.concat(dfs)

        return df
    

    def _df_registros(self, df):
        dias = [col for col in df.columns if 'Dia' in col]
        
        df_melted = df.melt(id_vars=['Municipios', 'Anos', 'Meses'], value_vars=dias, 
                            var_name='Dia_col', value_name='registros')
        
        df_melted['Dia'] = df_melted['Dia_col'].str.extract('(\d+)', expand=False).astype(int)
        
        df_melted['data'] = pd.to_datetime(df_melted['Anos'].astype(str) + '-' +
                                        df_melted['Meses'].astype(str).str.zfill(2) + '-' +
                                        df_melted['Dia'].astype(str).str.zfill(2), errors='coerce')
        
        df_result = df_melted[['Municipios', 'data', 'registros']]
    
   
        nome_arquivo = 'registros.csv'
        caminho_bronze = self._caminho_destino(nome_arquivo)

        df_result.to_csv(caminho_bronze, index=False)
    
    def _df_municipios(self, df):
        df_municipios = pd.DataFrame()
        df_municipios['Munipios'] = df.Municipios.unique()
        df_municipios['id'] = range(1, df_municipios.shape[0] + 1)

        nome_arquivo = 'municipios.csv'
        caminho_bronze = self._caminho_destino(nome_arquivo)

        df_municipios.to_csv(caminho_bronze, index=False)

    def _df_postos(self, df):
        colunas = ['Municipios', 'Postos', 'Latitude', 'Longitude']
        df_postos = df[colunas].drop_duplicates(subset=['Postos'])
        df_postos['id'] = range(1, df_postos.shape[0] + 1)

        nome_arquivo = 'postos.csv'
        caminho_bronze = self._caminho_destino(nome_arquivo)

        df_postos.to_csv(caminho_bronze, index=False)
    
    def _caminho_destino(self, nome_arquivo):
        caminho_bronze = os.path.join(self.dir_data_bronze, nome_arquivo)
        return caminho_bronze