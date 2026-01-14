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
            except mysql.connector.Error as err:
                raise err
     
    
    def modificar_paciente(self):
        pass
    
    def mostrar_paciente_por_id(self, paciete_id: int):
        with self.db_conn.connect_to_mysql() as conn:
            try:
                cursor = conn.cursor()
                query = f'select id_paciente, nombre, apellido, edad, obra_social,telefono from {self.db_name}.paciente where id_paciente = %s'
                cursor.execute(query, (paciete_id,))
                row = cursor.fetchone()
                print(row)
                
                
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
    
    
    