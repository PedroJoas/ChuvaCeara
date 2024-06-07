from transform_to_bronze import Tranformador_raw 
import os


caminho_data_bronze = 'data/bronze/csv'
os.makedirs(caminho_data_bronze, exist_ok=True)

transformador = Tranformador_raw(caminho_data_bronze)

transformador.TrataDados()

