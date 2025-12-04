import mysql.connector
from mysql.connector import errorcode
from dominio.paciente import Paciente
from dao.interfaz_dao.interfaz_paciente_dao import PacienteDAOInterfaz
from db.db_conn import DBConn

class PacienteDAO(PacienteDAOInterfaz):
    
    def __init__(self, db_conn: DBConn):
        self.db_conn = db_conn.connect_to_mysql()
        self.db_name = db_conn.get_data_base_name()
        
    def registrar_paciente(self, paciente: Paciente):
        with self.db_conn as conn:
            try:
                cursor = conn.cursor()
                
                query = f'instert into {self.db_name}.paciente (nombre,apellido,edad,obra_social,telefono) VALUES (%s, %s, %s, %s, %s)'
                cursor.execute(query,(paciente.nombre,paciente.apellido,paciente.edad,paciente.obra_social,paciente.telefono))
                
                conn.commit()
            except mysql.connector.Error as err:
                raise err
     