from abc import abstractmethod
from abc import ABC


class turnoDAO(ABC):
    @abstractmethod
    def registrar_turno(self, turno : object): #recibe un objeto, turno.
     pass

    @abstractmethod
    def modificar_turno(self, objeto: object): #recibe un objeto turno. 
        pass

    @abstractmethod
    def eliminar_turno(self, id_turno = int): #recibe un id y elimina el turno
        pass
    
    
    @abstractmethod
    def obtener_turno(self, id_turno = int) #recibe el id del turno y muestra sus datos.

    @abstractmethod
    def visualizar_turnos(self):
        pass