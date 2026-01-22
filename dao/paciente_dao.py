import mysql.connector
from mysql.connector import errorcode
from dominio.paciente import Paciente
from dao.interfaz_dao.interfaz_paciente_dao import PacienteDAOInterfaz
from db.db_conn import DBConn

class PacienteDAO(PacienteDAOInterfaz):
    
    def __init__(self, db_conn: DBConn):
        self.db_conn = db_conn
        self.db_name = db_conn.get_data_base_name()
        
    def registrar_paciente(self, paciente: Paciente):
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                
                query = f'insert into {self.db_name}.paciente (nombre,apellido,edad,obra_social,telefono) VALUES (%s, %s, %s, %s, %s)'
                cursor.execute(query,(paciente.nombre,paciente.apellido,paciente.edad,paciente.obra_social,paciente.telefono))
                
                conn.commit()
                
                id_del_paciente = cursor.lastrowid
                return id_del_paciente
                
                
            except mysql.connector.Error as err:
                raise err
     
     
    def eliminar_paciente(self, paciente_id: int ):
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = f'delete from {self.db_name}.paciente where id_paciente =%s'
                cursor.execute(query, (paciente_id,))
                
                conn.commit()
                lineas_afectadas = cursor.rowcount
                return lineas_afectadas
                
            except mysql.connector.Error as err:
                raise err
     
    
    
    def mostrar_paciente_por_id(self, paciete_id: int):
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = f'select id_paciente, nombre, apellido, edad, obra_social,telefono from {self.db_name}.paciente where id_paciente = %s'
                cursor.execute(query, (paciete_id,))
                row = cursor.fetchone()
                return row
                
            except mysql.connector.Error as err:
                raise err
            
    
    def mostrar_todos_pacientes(self) -> list:
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = f'select * from {self.db_name}.paciente'
                cursor.execute(query)
                rows = cursor.fetchall()
                for x in rows:
                    print(x)
                conn.close()
            except mysql.connector.Error as err:
                raise err
    
    
    def mostrar_id_nombre_apellido(self) -> list:
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = f'select id_paciente, nombre, apellido from {self.db_name}.paciente'
                cursor.execute(query)
                rows = cursor.fetchall()
                return rows
            
            except mysql.connector.Error as err:
                raise err    
            
            
    def modificar_paciente(self, paciente : Paciente):
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                
                query = f'update {self.db_name}.paciente set nombre =%s, apellido =%s, edad =%s, obra_social =%s, telefono =%s where id_paciente =%s'
                
                values = (paciente.nombre,paciente.apellido,paciente.edad,paciente.obra_social,paciente.telefono,paciente.id_paciente)
                
                cursor.execute(query,values)
                conn.commit()
                
                lineas_afectadas = cursor.rowcount
                return lineas_afectadas
            
            except mysql.connector.Error as err:
                raise err            
            
    def modificar_nombre_paciente(self, paciente_id: int, nombre: str):
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                
                query = f'update {self.db_name}.paciente set nombre =%s where id_paciente = %s'
                values = (nombre,paciente_id)
                
                cursor.execute(query,values)
                conn.commit()
                
                lineas_afectadas = cursor.rowcount
                return lineas_afectadas
            
            except mysql.connector.Error as err:
                raise err


    def obtener_instancia_paciente_por_id(self, paciete_id: int):
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = f'select id_paciente, nombre, apellido, edad, obra_social,telefono from {self.db_name}.paciente where id_paciente = %s'
                cursor.execute(query, (paciete_id,))
                row = cursor.fetchone()
                return row
                
            except mysql.connector.Error as err:
                raise err