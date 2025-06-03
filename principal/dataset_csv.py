import pandas as pd 
from principal.base_dataset import Dataset

class DatasetCSV(Dataset):
    # Inicializa el dataset de la fuente de datos CSV
    def __init__(self, fuente):
        super().__init__(fuente)

    # Carga los datos desde la fuente de datos en el archivo CSV
    def load_data(self):
        # controla los error al abrir el archivo
        try:
            df = pd.read_csv(self.fuente)
            self.data = df
            # si los datos son validados los transforma
            if self.validate_data():
                self.transform_data()
        except Exception as e:
            print(f'error al cargar los datos: {e}')