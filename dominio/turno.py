from datetime import datetime

class Turno:
    def __init__(self,id_turno,id_paciente,id_resonador,fecha_hora: datetime,nombre_estudio,):
        
        self.__id_turno = id_turno
        self.__id_paciente = id_paciente
        self.__id_resonador = id_resonador
        self.__fecha_hora = fecha_hora
        self._nombre_estudio = nombre_estudio
        
        
        
    @property
    def id_turno(self):
        return self.__id_turno
    
    @property
    def id_paciente(self):
        return self.__id_paciente
    
    @property
    def id_resonador(self):
        return self.__id_resonador
    
    @property
    def fecha_hora(self):
        return self.__fecha_hora
    
    @fecha_hora.setter
    def fecha_hora(self,nueva_fecha_hora):
        self.__fecha_hora = nueva_fecha_hora
        
    @property
    def nombre_estudio(self):
        return self._nombre_estudio
    
    @nombre_estudio.setter
    def nombre_estudio(self,nuevo_nombre):
        self._nombre_estudio = nuevo_nombre
        
        
    