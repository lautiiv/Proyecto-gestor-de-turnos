from abc import abstractmethod
from abc import ABC
from dominio.turno import Turno
from datetime import datetime

class TurnoDAO_Interfaz(ABC):
    @abstractmethod
    def registrar_turno(self, turno : Turno)-> int: 
        #recibe un objeto, turno. devuelve un int que es el id del turno.
     pass

    #metodos no previstos
    @abstractmethod
    def listar_turnos_con_paciente(self)-> list:
        pass
    
    """---------------------------------------------------------------------------------------------------"""
    @abstractmethod
    def verificar_disponibilidad_horario_dao(self,fecha: datetime, id_resonador: int) -> bool:
        #Verifica si un resonador en ese horario esta ocupado o libre, devuelve un true: si esta ocupado, false si esta libre
        pass
    
    @abstractmethod
    def listar_turnos_con_paciente(self)-> list:
        #Devuelve una lista que se obtiene con consulta JOIN
        # informacion paciente: Nombre,apellido, informacion turno: nombre_estudio, estado, id_turno
        pass
    
    @abstractmethod
    def informacion_turno_por_id_turno(self, id_turno)-> tuple:
        #Devuelve una tupla que se obtiene con consulta JOIN
        #Recibe el id_turno y devuelve nombre, apellido, nombre_estudio, fecha y resonador
        pass
        
    @abstractmethod
    def informacion_turno_por_id_paciente(self, id_paciente: int)-> list :
        ##recibe un id_paciente, realiza un join para retornar una lista con los estudios del paciente
        #La informacion es nombre_estudio, fecha y en que equipo se realiza
        pass
    
    @abstractmethod
    def datos_turno_por_id_turno(self, id_turno) -> tuple:
        ##recibe un ID_TURNO, devuelve todos los datos del turno, permite instanciarlo en caso de querer hacerlo
        pass
    
    @abstractmethod
    def modificar_estado_turno_dao(self, id_turno: int, estado: str)-> int:
    #Recibe un id_turno y el nuevo estado del turno. Este puede ser, activo o cancelado o confirmado 
    #Devuelve el numero de lineas afectadas por el update.
        pass
    
    @abstractmethod
    def ver_turnos_por_dia(self, fecha_inicio: datetime, fecha_fin: datetime) -> list:
        #Realiza una consulta join, recibe la fecha inicio y fecha fin del dia.
        #Devuelve una lista con informacion: fecha, nombre_estudio, nombre, apellido, equipo.
        pass
    
    @abstractmethod
    def nombre_equipo(self, id_resonador)-> tuple:
        #Recibe id_resonador y devuelve el nombre del equipo
        pass
    
    @abstractmethod
    def actualizar_turno_dao(self, id_turno, nueva_fecha, nuevo_resonador) -> int:
        #Actualiza fecha y el resonador a traves del id_resonador
        #Retorna las lineas afectadas
        pass
    
    
    