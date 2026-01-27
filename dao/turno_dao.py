import mysql.connector
from mysql.connector import errorcode
from dominio.turno import Turno
from dao.interfaz_dao.interfaz_turno_dao import TurnoDAO_Interfaz
from db.db_conn import DBConn
from datetime import datetime

class TurnoDAO(TurnoDAO_Interfaz):
    def __init__(self, db_conn : DBConn):
        self.db_conn = db_conn
        self.db_name = db_conn.get_data_base_name()
        
    def registrar_turno(self, turno : Turno):
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = f'insert into {self.db_name}.turno (id_paciente,id_resonador,fecha,nombre_estudio) VALUES (%s, %s, %s, %s)'
                values = (turno.id_paciente,turno.id_resonador,turno.fecha_hora,turno.nombre_estudio)
                
                cursor.execute(query,values)
                conn.commit()
                
                id_turno = cursor.lastrowid
                
                return id_turno
            except mysql.connector.Error as err:
                raise(err)
            
    def verificar_disponibilidad_horario_dao(self,fecha: datetime, id_resonador: int) -> bool:
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                
                query = f'SELECT COUNT(*) from {self.db_name}.turno WHERE fecha = %s and id_resonador = %s'
                
                cursor.execute(query,(fecha,id_resonador))
                
                resultado = cursor.fetchone()
                cantidad = resultado[0]
                
                return cantidad > 0
            except mysql.connector.Error as err:
                raise err    
            
    
    def modificar_turno(self, turno : Turno):
        pass
        
    def cancelar_turno(self):
        pass
    
    def obtener_turno(self):
        pass
    
    def visualizar_turnos(self):
        pass
        