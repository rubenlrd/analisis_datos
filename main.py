from os import path
from principal.dataset_csv import DatasetCSV
from principal.dataset_excel import DatasetExcel
from principal.dataset_api import DatasetAPI
from principal.dataset_json import DatasetJson
from conexion.data_conexion import DataSaver

def guardar_datos(data, nombre_archivo):
    #Guarda el DataFrame en la base de datos.
    db = DataSaver()
    db.save_dataframe(data, nombre_archivo)
    print(f"Datos del archivo {nombre_archivo} guardados en la base de datos.")


print ('Bienvenidos al sistema de carga de datos')
print ('Los archivos a migrar deben estar en la carpeta Archivos')
ejecucion = True


# Ejecuta el programa hasta que el usuario decida salir
while ejecucion:
    print('--------------- Menú ----------------')
    print('1. Cargar datos desde un archivo CSV')
    print('2. Cargar datos desde un archivo Excel')
    print('3. Cargar datos desde un archivo json')
    print('4. Cargar datos desde una API')
    print('5. Salir')
    opcion = input('Seleccione una opción: ')
    
    # eligir entra las opcciones a ejecutar
    if opcion == '1':
        # ejecuta las instrucciones para cargar el archivo csv
        ejecución = True
        nombre_archivo = input("Ingrese nombre del archivo csv: ")
        separador = input("Ingrese el separador del archivo csv (, - ;): ")
        # Ruta del la ubicación del archivo
        csv_path = path.join(path.dirname(__file__), "archivos", nombre_archivo)
        # cargar y transformar
        csv = DatasetCSV(csv_path, separador)
        csv.cargar_datos()
        csv.show_summary()
        # Guardar en base de datos
        guardar_datos(csv.data, nombre_archivo)
        # db = DataSaver()
        # db.save_dataframe(csv.data, nombre_archivo)
        

    elif opcion == '2':
        # ejecuta las instrucciones para cargar el archivo excel
        ejecución = True
        nombre_archivo = input("Ingrese nombre del archivo excel: ")
        # Ruta del la ubicación del archivo
        excel_path = path.join(path.dirname(__file__), "archivos", nombre_archivo)
        # cargar y transformar 
        excel = DatasetExcel(excel_path)
        excel.cargar_datos()
        excel.show_summary()
        # Guardar en la base de datos 
        guardar_datos(excel.data, nombre_archivo)
        #db = DataSaver()
        #db.save_dataframe(excel.data, nombre_archivo)

    elif opcion == '3':
        # ejecuta las instrucciones para cargar el archivo JSON
        ejecución = True
        nombre_archivo = input("Ingrese nombre del archivo JSON: ")
        # Ruta del la ubicación del archivo
        json_path = path.join(path.dirname(__file__), "archivos", nombre_archivo)
        # cargar y transformar 
        archJson= DatasetJson(json_path)
        archJson.cargar_datos()
        archJson.show_summary()
        # Guardar en base de datos
        guardar_datos(archJson.data, nombre_archivo)
        # db = DataSaver()
        # db.save_dataframe(archJson.data, nombre_archivo)
    elif opcion == '4':
        # ejeccuta las instrucciones para cargar la api
        ejecucion = True
        # ruta de la api
        url = input("Ingrese la Url de la API: ")
        # carga y transforma
        api = DatasetAPI(url)
        api.cargar_datos()
        api.show_summary()
        # Guardar en base de datos
        # db = DataSaver()
        # db.save_dataframe(api.data, url)
        guardar_datos(api.data, url)
    elif opcion == '5':
        print('Saliendo del sistema...')
        ejecucion = False
        break
    else:
        print('Opción no válida, intente de nuevo.')


