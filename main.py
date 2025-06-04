from os import path
from principal.dataset_csv import DatasetCSV

nombre_archivo = input("Ingrese nombre del archivo: ")
# Ruta del la ubicación del archivo csv
csv_path = path.join(path.dirname(__file__), "archivos", nombre_archivo)

# cargar y transformar 
csv = DatasetCSV(csv_path)
csv.cargar_datos()

# Guardar en base de datos
