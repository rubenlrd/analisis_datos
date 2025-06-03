# Clase base de donde heredaran los datasets api, csv, txt, excel
from abc import ABC, abstractmethod

class Dataset(ABC):
    # Inicializa el dataset con la fuente de datos o sea seria el constructor
    def __init__(self, fuente):
        self.__fuente = fuente 
        self.__datos = None

    @property #actua como un getter 
    def data(self):
        return self.__datos
    
    @data.setter # actua como setter
    def data(self, value):
        # validaciones
        self.__datos = value

    @property
    def fuente(self):
        return self.__fuente
    
    @abstractmethod    
    def load_data(self):
        # Carga los datos desde la fuente
        pass
    
    def validate_data(self):
        # Valida los datos cargados
        pass
    
    def transform_data(self):
        # Transforma los datos cargados
        pass
    
    def show_summary(self):
        # Muestra un resumen de los datos
        pass