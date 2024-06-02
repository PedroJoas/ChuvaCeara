import urllib3
import zipfile
import os
import time

# URL dos dados da FUNCEME
url = 'https://cdn.funceme.br/calendario/postos/postos.zip'
raw_caminho = 'data/raw/'
nome_arquivo = 'postos.zip'

caminho_arquivo_zip = os.path.join(raw_caminho, nome_arquivo)
try:
    # Baixando arquivo da url
    http = urllib3.PoolManager()
    with http.request('GET', url, preload_content=False) as response, open(caminho_arquivo_zip, 'wb') as out_file:
        out_file.write(response.data)
except Exception as e:
    print(f"Erro ao baixar o arquivo: {e}")


try:
    
    while not os.path.exists(caminho_arquivo_zip):
        print("Aguardando arquivo zip ser baixado!")
        time.sleep(3)
    
    os.makedirs(raw_caminho + 'txt/', exist_ok=True)
    
    # Unzipped arquivo baixado
    with zipfile.ZipFile(caminho_arquivo_zip, 'r') as zip_ref:
        zip_ref.extractall(raw_caminho + 'txt/')
        
    # Removendo arquivo
    os.remove(caminho_arquivo_zip)
except Exception as e:
    print(f"Erro ao extrair o arquivo: {e}")
