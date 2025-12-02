class Paciente:
    def __init__(self,id_paciente,nombre,apellido,edad,obra_social,telefono):
        
        self.__id_paciente = id_paciente
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self._obra_social = obra_social
        self.__telefono = telefono
    
    
    @property
    def id_paciente(self):
        return self.__id_paciente
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self,nuevo_apellido):
        self.__apellido = nuevo_apellido
        
    @property
    def edad(self):
        return self.__edad
        
    @edad.setter
    def edad(self,nueva_edad):
        self.__edad = nueva_edad
        
    @property
    def obra_social(self):
        return self._obra_social
    
    @obra_social.setter
    def obra_social(self,nueva_obra_social):
        self._obra_social = nueva_obra_social
        
    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self,nuevo_telefono):
        self.__telefono = nuevo_telefono
    
    