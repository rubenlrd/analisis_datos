import pandas as pd
from principal.dataset_base import Dataset

class DatasetExcel(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)
    
    def cargar_datos(self):
        try:
            df = pd.read_excel(self.fuente)
            self.data = df
            print(f'Datos cargados correctamente desde {self.fuente}')
            # print(self.data.head())
            # si los datos son validados los transforma
            if self.validate_data():
                self.transform_data()
            #return super().cargar_datos()
        except Exception as e:
            print(f"Error al cargar datos desde Excel: {e}")
            return False