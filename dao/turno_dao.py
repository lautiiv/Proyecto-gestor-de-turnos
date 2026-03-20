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
                query = f'insert into {self.db_name}.turno (id_paciente,id_resonador,fecha,nombre_estudio,estado) VALUES (%s, %s, %s, %s, %s)'
                values = (turno.id_paciente,turno.id_resonador,turno.fecha_hora,turno.nombre_estudio,turno.estado)
                
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
            
    def listar_turnos_con_paciente(self)-> list:
        #Devuelve una lista que se obtiene con consulta JOIN, informacion paciente: Nombre,apellido, informacion turno: nombre_estudio, estado, id_turno
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
            
                query = f'SELECT t.id_turno, t.nombre_estudio, p.nombre, p.apellido, t.estado FROM {self.db_name}.turno t JOIN {self.db_name}.paciente p on (t.id_paciente = p.id_paciente)'
            
                cursor.execute(query)
                rows = cursor.fetchall()
                return rows
            except mysql.connector.Error as err:
                raise err
    
    def informacion_turno_por_id_turno(self, id_turno):
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                
                query = f"""SELECT p.nombre, p.apellido, t.nombre_estudio, t.fecha, r.nombre_equipo 
                FROM {self.db_name}.turno t 
                join {self.db_name}.paciente p on t.id_paciente = p.id_paciente
                join {self.db_name}.resonador r on t.id_resonador = r.id_resonador
                where t.id_turno = %s"""
                
                valor = id_turno
                
                cursor.execute(query,(valor,))
                
                resultado = cursor.fetchone()
                
                return resultado
            except mysql.connector.Error as err:
                raise err
                  
    def informacion_turno_por_id_paciente(self, id_paciente: int)-> list :
        #recibe un id_paciente, realiza un join para retornar una lista con los estudios del paciente
        #La informacion es nombre_estudio, fecha y en que equipo se realiza
        
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                
                query = f"""select t.nombre_estudio, t.fecha, r.nombre_equipo
                from {self.db_name}.turno t
                join {self.db_name}.resonador r on t.id_resonador = r.id_resonador
                where id_paciente = %s"""
                
                cursor.execute(query,(id_paciente,))
                
                rows = cursor.fetchall()
                
                return rows
            except mysql.connector.Error as err:
                raise err
    
    def datos_turno_por_id_turno(self, id_turno) -> tuple:
        #recibe un ID_TURNO, devuelve todos los datos del turno, permite instanciarlo en caso de querer hacerlo.
        
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = f'select id_turno, id_paciente, id_resonador, fecha, nombre_estudio, estado from {self.db_name}.turno where id_turno = %s'
                cursor.execute(query,(id_turno,))
            
                resultado = cursor.fetchone()
            
                return resultado
            except mysql.connector.Error as err:
                raise err
              
        
    def modificar_estado_turno_dao(self, id_turno: int, estado: str)-> int:
        #Recibe un id_turno y el nuevo estado del turno. Este puede ser, activo o cancelado o confir 
        #Devuelve el numero de lineas afectadas por el update.
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = f'UPDATE {self.db_name}.turno SET estado = %s WHERE id_turno = %s'
                
                cursor.execute(query, (estado,id_turno))
                conn.commit()
                lineas_afectadas = cursor.rowcount
                return lineas_afectadas
            except mysql.connector.Error as err:
                raise err                   
    
    def ver_turnos_por_dia(self, fecha_inicio: datetime, fecha_fin: datetime) -> list:
        
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = f"""SELECT t.fecha, t.nombre_estudio, p.nombre, p.apellido, r.nombre_equipo
                        FROM {self.db_name}.turno t
                        JOIN {self.db_name}.paciente p
                        ON t.id_paciente = p.id_paciente
                        JOIN {self.db_name}.resonador r
                        ON t.id_resonador = r.id_resonador
                        WHERE t.fecha >= %s and t.fecha < %s
                        ORDER BY (r.nombre_equipo) asc, (t.fecha) asc;
                        """
                        
                cursor.execute(query, (fecha_inicio,fecha_fin))
               
                rows = cursor.fetchall()
                return rows
            except mysql.connector.Error as err:
                raise err
    def nombre_equipo(self, id_resonador):
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = f'SELECT nombre_equipo FROM {self.db_name}.resonador WHERE id_resonador = %s'
                cursor.execute(query,(id_resonador,))
                
                resultado = cursor.fetchone()
                return resultado
            except mysql.connector.Error as err:
                raise err
   
    def actualizar_turno_dao(self, id_turno, nueva_fecha, nuevo_resonador):
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = f'UPDATE {self.db_name}.turno SET fecha = %s, id_resonador = %s WHERE id_turno = %s'
                cursor.execute(query,(nueva_fecha,nuevo_resonador,id_turno))
                conn.commit()
                lineas_afectadas = cursor.rowcount
                return lineas_afectadas
            except mysql.connector.Error as err:
                raise err