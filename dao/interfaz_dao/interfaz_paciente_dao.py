from abc import ABC, abstractmethod
from dominio.paciente import Paciente

class PacienteDAOInterfaz(ABC):
    @abstractmethod
    def registrar_paciente(self, paciente: Paciente): # recibe una instancia del objeto paciente. Devuelve el id_del paciente.
        pass
    
    @abstractmethod
    def modificar_paciente(self, paciente : Paciente): #recibe el id del paciente a modificar - devuelve un bool
        pass
    
    @abstractmethod
    def eliminar_paciente(self, paciente_id : int): # rebice el id del paciente a eliminar devuelve un bool.
        pass
        
    @abstractmethod
    def mostrar_paciente_por_id(self, paciente_id : int): #recibe el id del paciente a eliminar
        pass
    
    @abstractmethod
    def mostrar_todos_pacientes(self) -> list[Paciente]:
        pass
    
