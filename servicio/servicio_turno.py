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
        
        
        