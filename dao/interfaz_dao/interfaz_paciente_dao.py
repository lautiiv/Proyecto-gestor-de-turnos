from abc import ABC, abstractmethod

class DataAccessDAO(ABC):
    @abstractmethod
    def registrar_paciente(self):
        pass
    
    @abstractmethod
    def modificar_paciente(self):
        pass
    
    @abstractmethod
    def eliminar_paciente(self):
        pass
        
    @abstractmethod
    def mostrar_datos_paciente(self):
        pass
    
