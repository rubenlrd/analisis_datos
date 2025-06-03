from os import path
from principal.dataset_csv import DatasetCSV

file_name = input("Ingres nombre del archivo: ")
# Ruta del la ubicación del archivo csv
csv_path = path.join(path.dirname(__file__), "archivos", file_name)

# cargar y transformar 
csv = DatasetCSV(csv_path)
csv.load_data()

# Guardar en base de datos
