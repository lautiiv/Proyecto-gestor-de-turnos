from dominio.paciente import Paciente
from db.db_conn import DBConn
from dao.paciente_dao import PacienteDAO

class Servicios_Pacientes:
    def __init__(self, db : DBConn):
        self.db = db
        self.dao = PacienteDAO(db)
        
    def registrar_paciente(self, nombre: str, apellido: str, edad: int, obra_social: str, telefono:str,):
            
            nombre = nombre.strip()
            apellido = apellido.strip()
            obra_social = obra_social.strip()
            telefono = telefono.strip()
            
            #Validaciones para nombre y apellido
            
            if not nombre or not apellido:
                raise ValueError("El nombre y el apellido no pueden estar vacios")
            
            elif not nombre.isalpha() or not apellido.isalpha():
                raise ValueError("El nombre no puede contener numeros")
            
            elif len(nombre) <= 2 or len(nombre) > 50:
                raise ValueError("El nombre tiene que tener entre 3 y 50 digitos")
            
            #Validaciones para edad
            
            if not edad:
                raise ValueError("La edad no puede estar vacia")
            elif edad < 0:
                raise ValueError("La edad no puede ser menor a 0")
            elif edad > 130:
                raise ValueError("La edad que ingresaste es superior al limite posible")
            
            
            #Validaciones para obra_social
            
            if not obra_social:
                raise ValueError("La obra oscial no puede estar vacia")
            
            elif len(obra_social) > 50:
                raise ValueError("El nombre de la obra social no puede tener mas de 50 digitos")
            
            # Validaciones para telefono
            
            if not telefono:
                raise ValueError("El telefono no puede estar vacio")
            
            elif not telefono.isdigit():
                raise ValueError("El telefono solo puede contener numeros")
            
            elif len(telefono) < 5 or len(telefono) > 15:
                raise ValueError("El numero de telefono tiene que tener entre 5 y 15 digitos")            
            
            nuevo_paciente = Paciente(
                nombre,
                apellido,
                edad,
                obra_social,
                telefono
                )
            
            try:
                id_nuevo_paciente = self.dao.registrar_paciente(nuevo_paciente)
                nuevo_paciente.id_paciente = id_nuevo_paciente
                print("Paciente registrado con exito, a continuacion le muestro ID correspondiente")
                return id_nuevo_paciente
            except Exception as e:
                raise ValueError(F"ERROR AL REGISTRAR PACIENTE: {e}")
            
            
    def mostrar_pacientes(self):
        lista_de_pacientes = self.dao.mostrar_todos_pacientes()
        return lista_de_pacientes
    
    def mostrar_paciente_por_id(self, ID):
        
        datos_del_paciente = self.dao.mostrar_paciente_por_id(ID)
        
        if not datos_del_paciente:
            print("El ID ingresado no coincide con ningun usuario")
        else:
            print(datos_del_paciente)
    
    def eliminar_paciente(self,ID):
        
        print("Se intenta eliminar el Paciente con ID", ID)
        paciente_eliminado = self.dao.eliminar_paciente(ID)
            
        if paciente_eliminado > 0:
            print("Paciente eliminado con exito")
        else:
            print("Error al eliminar el paciente, id incorrecto")
        
    def mostrar_id_nombre_apellido_servicio(self):
        datos_pacientes = self.dao.mostrar_id_nombre_apellido()
        for x in datos_pacientes:
            print(f"ID: {x[0]}, {x[1]}, {x[2]}")
          
    def obtener_instancia_paciente_por_id(self,ID_PACIENTE):
        paciente_dao = self.dao.obtener_instancia_paciente_por_id(ID_PACIENTE)
        
        paciente = Paciente(
            nombre=paciente_dao[1],
            apellido=paciente_dao[2],
            edad=paciente_dao[3],
            obra_social=paciente_dao[4],
            telefono=paciente_dao[5],
            id_paciente=paciente_dao[0])
        
            
        return paciente
    
    def update_paciente(self, paciente: Paciente):
        pass