import pandas as pd 
from principal.dataset_base import Dataset

class DatasetJson(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)
    
    def cargar_datos(self):
        # controla los error al abrir el archivo
        try:
            df = pd.json_normalize(pd.read_json(self.fuente, orient='records', lines=True))
            # df = pd.read_json(self.fuente, orient='records', lines=True)
            self.data = df
            print(f'Datos cargados correctamente desde {self.fuente}')
            print(self.data.head())
            # si los datos son validados los transforma
            if self.validate_data():
                self.transform_data()
        except Exception as e:
            print(f'error al cargar los datos: {e}')
        #return super().cargar_datos()