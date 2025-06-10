import requests
import pandas as pd
from principal.dataset_base import Dataset

class DatasetAPI(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)
    
    def cargar_datos(self):
        try:
            print(f"Conectando a API: {self.fuente}")
            response = requests.get(self.fuente, timeout=30)
            
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
                
                # Función mejorada para convertir listas a string - falta revisar por que no convierte como yo quiero
                def lista_a_string(x):
                    if pd.isna(x):  # Manejar valores NaN
                        return ''
                    elif isinstance(x, list):
                        # Manejar listas vacías
                        if not x:
                            return ''
                        # Convertir elementos de la lista manejando None y otros tipos
                        elementos_str = []
                        for item in x:
                            if pd.isna(item) or item is None:
                                elementos_str.append('')
                            elif isinstance(item, dict):
                                # Si el elemento es un diccionario, convertirlo a string JSON
                                elementos_str.append(str(item))
                            else:
                                elementos_str.append(str(item))
                        return ', '.join(elementos_str)
                    elif isinstance(x, dict):
                        # Si es un diccionario, convertirlo a string
                        return str(x)
                    else:
                        return str(x) if x is not None else ''
                
                # Aplicar transformación a todas las columnas
                print("Convirtiendo datos complejos a texto plano...")
                for col in df.columns:
                    # Verificar si la columna contiene listas, diccionarios o valores complejos
                    tiene_listas = df[col].apply(lambda x: isinstance(x, (list, dict))).any()
                    if tiene_listas:
                        print(f"Convirtiendo columna '{col}' a texto plano")
                        df[col] = df[col].apply(lista_a_string)
                
                # Asegurar que todos los valores sean strings o números simples
                for col in df.columns:
                    if df[col].dtype == 'object':
                        df[col] = df[col].astype(str)
                
                self.data = df
                print(f"API cargada exitosamente. Filas: {len(df)}, Columnas: {len(df.columns)}")
                print(f"Columnas disponibles: {list(df.columns)}")
                
                # Mostrar tipos de datos para verificación
                print("\nTipos de datos por columna:")
                for col in df.columns:
                    print(f"  {col}: {df[col].dtype}")
                
                # Validar y transformar datos si es necesario
                if self.validate_data():
                    self.transform_data()
                    
            else:
                print(f"Error HTTP {response.status_code}: {response.reason}")
                print(f"Respuesta del servidor: {response.text[:500]}")
                
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
            import traceback
            traceback.print_exc()
