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
                raise ValueError("ERROR AL REGISTRAR PACIENTE:", e)
            
            
    def mostrar_pacientes(self):
        lista_de_pacientes = self.dao.mostrar_todos_pacientes()
        return lista_de_pacientes