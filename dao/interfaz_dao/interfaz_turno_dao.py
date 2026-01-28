from abc import abstractmethod
from abc import ABC
from dominio.turno import Turno

class TurnoDAO_Interfaz(ABC):
    @abstractmethod
    def registrar_turno(self, turno : Turno): #recibe un objeto, turno. devuelve un int el id del turno.
     pass

    @abstractmethod
    def modificar_turno(self, turno: Turno): #recibe un objeto turno. devuelve un bool. #modificado.
        pass

    @abstractmethod
    def cancelar_turno(self, id_turno : int): #recibe un id y elimina el turno devuelve un bool
        pass
    
    
    @abstractmethod
    def obtener_turno(self, turno_id : int): #recibe el id del turno y muestra sus datos
        pass
    
    @abstractmethod
    def visualizar_turnos(self): #muestra todos los turnos
        pass
    
    #metodos no previstos
    @abstractmethod
    def listar_turnos_con_paciente(self)-> list:
        pass