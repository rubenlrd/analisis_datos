import requests
import pandas as pd
from principal.dataset_base import Dataset

class DatasetAPI(Dataset):
    def __init__(self, fuente):  # Corregido: __init__ en lugar de **init**
        super().__init__(fuente)
    
    def cargar_datos(self):
        try:
            print(f"Conectando a API: {self.fuente}")
            response = requests.get(self.fuente, timeout=30)  # Agregado timeout
            
            if response.status_code == 200:
                json_data = response.json()
                
                # Verificar si la respuesta es una lista o un diccionario
                if isinstance(json_data, list):
                    df = pd.json_normalize(json_data)
                elif isinstance(json_data, dict):
                    # Buscar la clave principal de datos
                    if 'data' in json_data:
                        df = pd.json_normalize(json_data['data'])
                    elif 'results' in json_data:
                        df = pd.json_normalize(json_data['results'])
                    else:
                        # Si no encuentra estructura conocida, usar todo el objeto
                        df = pd.json_normalize([json_data])
                else:
                    raise ValueError("Formato de respuesta no soportado")
                
                # Verificar si un valor es una lista
                def es_lista(x):
                    return isinstance(x, list)
                
                # Transformar todas las columnas tipo list a string
                def lista_a_string(x):
                    if isinstance(x, list):
                        return ', '.join(map(str, x))
                    return x  # Retornar el valor original si no es lista
                
                # Aplicar transformación a columnas que contienen listas
                for col in df.columns:
                    if df[col].apply(es_lista).any():
                        df[col] = df[col].apply(lista_a_string)
                
                self.data = df  # Corregido: usar 'data' en lugar de 'datos'
                print(f"API cargada exitosamente. Filas: {len(df)}, Columnas: {len(df.columns)}")
                print(f"Columnas disponibles: {list(df.columns)}")
                
                # Validar y transformar datos si es necesario
                if self.validate_data():
                    self.transform_data()
                    
            else:
                print(f"Error HTTP {response.status_code}: {response.reason}")
                print(f"Respuesta del servidor: {response.text[:500]}")  # Primeros 500 caracteres
                
        except requests.exceptions.Timeout:
            print("Error: Tiempo de espera agotado al conectar con la API")
        except requests.exceptions.ConnectionError:
            print("Error: No se pudo conectar con la API. Verifique la URL y su conexión a internet")
        except requests.exceptions.RequestException as e:
            print(f"Error de solicitud HTTP: {e}")
        except ValueError as e:
            print(f"Error en el formato de datos: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
            # Opcional: imprimir más detalles del error para debugging
            import traceback
            traceback.print_exc()
# import requests
# import pandas as pd
# from principal.dataset_base import Dataset


# class DatasetAPI(Dataset):
#     def __init__(self, fuente):
#         super().__init__(fuente)

#     def cargar_datos(self):
#         try:
#             response = requests.get(self.fuente)
#             if response.status_code == 200:
#                 df = pd.json_normalize(response.json())

#                 # Verificar si un vañor es una lista
#                 def es_lista(x):
#                     return isinstance(x, list)

#                 # Transformar todas las columnas tipo list a string
#                 def lista_a_string(x):
#                     if isinstance(x, list):
#                         return ', '.join(map(str, x))

#                 for col in df.columns:
#                     if df[col].apply(es_lista).any():
#                         df[col] = df[col].apply(lista_a_string)

#                 self.datos = df
#                 print("API cargada")

#                 if self.validate_data():
#                     self.transform_data()

#             else:
#                 print("Error al obtener datos de API")
#         except Exception as e:
#                 print(f"Error API. {e}")