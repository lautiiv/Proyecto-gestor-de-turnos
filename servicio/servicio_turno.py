from dominio.turno import Turno
from db.db_conn import DBConn
from dao.turno_dao import TurnoDAO
from datetime import datetime
from dao.paciente_dao import PacienteDAO

class Servicio_Turnos:
    def __init__(self, db : DBConn):
        self.db = db
        self.dao = TurnoDAO(db)
        self.paciente_dao = PacienteDAO(db)
        
    def validar_turno(self, turno : Turno):
        turno.nombre_estudio = turno.nombre_estudio.strip()
        
        #id_paciente,id_resonador,fecha_hora,nombre_estudio
        if not turno.id_paciente or not turno.id_resonador:
            raise ValueError("No puede faltar el id del paciente o del resonador")
        
        if turno.id_resonador < 1 or turno.id_resonador > 3:
            raise ValueError("El id del resonador tiene que ser 1-2-3")
        
        self.verificar_paciente_existe(turno.id_paciente)
        
        #Validaciones para nombre estudio
        
        if not turno.nombre_estudio:
            raise ValueError ("El nombre del estudio no puede estar vacio")
        
        if len(turno.nombre_estudio) > 50:
            raise ValueError("El nombre del estudio no puede tener mas de 50 caracteres")
        
        #Validaciones para hora
        
        if not turno.fecha_hora:
            raise ValueError("No puede estar vacia la fecha y hora")
        
        if turno.fecha_hora < datetime.now():
            raise ValueError("No puede registrarse el estudio en el pasado")
        
        hora = turno.fecha_hora.time()
        if hora.hour < 8 or hora.hour >=20:
            raise ValueError("Los turnos solo pueden ser entre las 08:00 y 20:00hs")
        
        if turno.fecha_hora.minute not in (0,30):
            raise ValueError("Los estudios tienen que ser cada 30 minutos")
        
        self.validar_disponibilidad_horario(turno.fecha_hora,turno.id_resonador)
        
    def verificar_paciente_existe(self,id):
        resultado = self.paciente_dao.verificar_paciente_existe(id)
        
        if resultado == False:
            raise ValueError("No se encontro paciente con ese ID")
        
    def validar_disponibilidad_horario(self,horario,id_resonador):
        resultado = self.dao.verificar_disponibilidad_horario_dao(horario,id_resonador)
        
        if resultado == True:
            raise ValueError("No se pudo registrar el turno porque ya esta ocupado ese horario en ese resonador")

    
    def registrar_turno(self, turno : Turno):
        self.validar_turno(turno)
        try:
            self.dao.registrar_turno(turno)
            print("Registrado")
        except ValueError as err:
            raise err
        
    def listar_pacientes(self):
        datos_pacientes = self.paciente_dao.mostrar_id_nombre_apellido()
        for x in datos_pacientes:
            print(f"ID: {x[0]}, {x[1]}, {x[2]}")
        
    def listar_id_turnos_pacientes(self):
        informacion_turnos = self.dao.listar_turnos_con_paciente()
        for valor in informacion_turnos:
            print(f'Nombre completo: {valor[2]} {valor[3]}, Estudio: {valor[1]}, ID_turno: {valor[0]} ')
        
    def informacion_turno(self, id_turno):
        informacion_del_turno = self.dao.informacion_turno_por_id_turno(id_turno)
        
        if  informacion_del_turno == None:
            raise ValueError("No se encontro un turno con ese ID")

        else:
            print(f'''\n== INFORMACION DEL TURNO == \nNombre: {informacion_del_turno[0]}, {informacion_del_turno[1]}\nEstudio: {informacion_del_turno[2]}\nFecha y hora: {informacion_del_turno[3]}\nEquipo: Resonador {informacion_del_turno[4]}''')
            
    def informacion_turno_por_id_paciente(self, id_paciente):
        
        #A traves de id_paciente trae nombre,apellido del paciente por dao_paciente. Con el mismo ID a traves de dao turno trae la lista de turnos que tenga asignado.
        #De esta forma con las dos consultas se muestra una vez el nombre del paciente y x veces los turnos que tenga dependiendo cuantos turnos tenga.
        
        turnos= self.dao.informacion_turno_por_id_paciente(id_paciente)
        nombre_paciente = self.paciente_dao.nombre_completo(id_paciente)
        
        if nombre_paciente is None:
            raise ValueError("\nNo se encontro paciente con ese id")
        
        if not turnos:
            print(f"No se encontraron turnos para el paciente {nombre_paciente[0]}, {nombre_paciente[1]}")
        
        print(f'== INFORMACION DEL TURNO == \n')
        print(f'Nombre: {nombre_paciente[0]}, {nombre_paciente[1]}\n')
        
        for estudio in turnos:
            print(f'Nombre estudio: {estudio[0]}\nFecha y hora: {estudio[1]}\nNombre del equipo: {estudio[2]}\n')
        return
