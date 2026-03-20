from abc import ABC, abstractmethod
from dominio.paciente import Paciente

class PacienteDAOInterfaz(ABC):
    @abstractmethod
    def registrar_paciente(self, paciente: Paciente): 
        # recibe una instancia del objeto paciente. Devuelve el id_del paciente.
        pass
    
    @abstractmethod
    def modificar_paciente(self, paciente : Paciente): 
        #recibe el paciente a modificar - devuelve un rowcount para ver lineas afectadas
        pass 
    
    @abstractmethod
    def eliminar_paciente(self, paciente_id : int)-> bool: 
        # recibe el id del paciente a eliminar devuelve un bool indicando si fue borrado o no.
        pass
        
    @abstractmethod
    def mostrar_paciente_por_id(self, paciente_id : int)-> tuple: 
        #recibe el id del paciente a  mostrar y devuelve los datos
        pass
    
    @abstractmethod
    def mostrar_todos_pacientes(self) -> list[Paciente]:
        #Al ser llamada devuelve una lista con toda la informacion de los pacientes.
        pass
    
    """------------------------------------------------------------------"""
    @abstractmethod
    def mostrar_id_nombre_apellido(self) -> list:
        #Devuelve una lista con ID_PACIENTE, nombre, apellido
        pass
    @abstractmethod
    def obtener_instancia_paciente_por_id(self, paciente_id: int) -> tuple:
        #Recibe ID_Paciente y devuelve todos los datos del paciente para instanciarlo posteriormente
        pass
        
    @abstractmethod
    def verificar_paciente_existe(self,id_paciente : int) -> bool:
        #Recibe el id_paciente y devuelve un bool indicando si el paciente existe o no
        pass
    
    @abstractmethod
    def nombre_completo(self,id_paciente: int) -> tuple:
        #Recibe id_paciente devuelve una tupla con el nombre, y el apellido
        pass