import os


class Tranformador_raw():

    dir_data_raw = 'data/raw/txt'

    def arquivos(self):
        return os.listdir(self.dir_data_raw)
