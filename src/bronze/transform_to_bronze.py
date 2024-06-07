import pandas as pd
import os
import re
from datetime import datetime


class Tranformador_raw():

    dir_data_raw = 'data/raw/txt'

    def _df_registros(df):
        dias = [col for col in df.columns if 'Dia' in col]
        dfs = []

        for dia_col in dias:
            aux_df = pd.DataFrame()
            dia_num = int(re.sub('[^0-9]', '', dia_col))
            datas = []

            for ano, mes in zip(df['Anos'], df['Meses']):
                try:
                    data = pd.to_datetime(f'{ano}-{mes:02d}-{dia_num:02d}')

                except ValueError:
                    data = pd.NaT

                datas.append(data)
            
            aux_df['municipios'] = df['Municipios']
            aux_df['data'] = datas
            aux_df['registros'] = df[dia_col]
            
            dfs.append(aux_df)
        # salvar csv ao invés de retornar 
        return dfs
    
    

