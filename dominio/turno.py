class Turno:
    def __init__(self,id_turno,id_paciente,id_resonador,fecha,estudio,estado_del_turno):
        
        self.__id_turno = id_turno
        self.__id_paciente = id_paciente
        self.__id_resonador = id_resonador
        self.__fecha = fecha
        self._nombre_estudio = estudio
        self._estado_del_turno = estado_del_turno
        
        
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
    def fecha(self):
        return self.__fecha
    
    
    @fecha.setter
    def fecha(self,nueva_fecha):
        self.fecha = nueva_fecha
        
        
    @property
    def nombre_estudio(self):
        return self._nombre_estudio
    
    @nombre_estudio.setter
    def nombre_estudio(self,nuevo_nombre):
        self._nombre_estudio = nuevo_nombre
        
    @property
    def estado_del_turno(self):
        return self._estado_del_turno
    
    @estado_del_turno.setter
    def estado_del_turno(self,nuevo_estado):
        self._estado_del_turno = nuevo_estado
        
    