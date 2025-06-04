import pandas as pd 
from principal.dataset_base import Dataset

class DatasetCSV(Dataset):
    # Inicializa el dataset de la fuente de datos CSV
    def __init__(self, fuente, separador):
        super().__init__(fuente)
        self.separa = separador

    # Carga los datos desde la fuente de datos en el archivo CSV
    def cargar_datos(self):
        # controla los error al abrir el archivo
        try:
            df = pd.read_csv(self.fuente, sep=self.separa, encoding='utf-8')
            self.data = df
            print(f'Datos cargados correctamente desde {self.fuente}')
            # si los datos son validados los transforma
            if self.validate_data():
                self.transform_data()
        except Exception as e:
            print(f'Error al cargar los datos: {e}')