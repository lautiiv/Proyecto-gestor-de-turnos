import pytest
import mysql.connector
from mysql.connector import errorcode
from db.db_conn import DBConn

from dao.paciente_dao import PacienteDAO
from dominio.paciente import Paciente


@pytest.fixture(scope="module")
def conn():
    db_conn = DBConn("test_config.ini")
    conn = db_conn.connect_to_mysql()
    
    try:
        with conn.cursor() as cursor:
            
            cursor.execute("CREATE DATABASE IF NOT EXISTS test_turnos")
            cursor.execute("USE test_turnos")
            
            cursor.execute("CREATE TABLE IF NOT EXISTS test_turnos.paciente (id_paciente int primary key not null auto_increment,nombre varchar(50) not null, apellido varchar(50) not null, edad int not null, obra_social varchar(50) not null, telefono varchar(20) not null)")
            
            cursor.execute("DELETE FROM test_turnos.paciente")
            conn.commit()
            
        yield conn
            
        with conn.cursor() as cursor:
            cursor.execute("DROP DATABASE IF EXISTS test_turnos")
            conn.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            raise("Usuario o password invalidos")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            raise("La base de datos no existe")
        else:
            raise(err)
    return None            

class TestPacienteDao:
    #HELPER crea paciente para las siguientes pruebas
    def crear_paciente(self,conn):
        
        with conn.cursor as cursor:
            cursor.execute("INSERT INTO test_turnos.paciente (nombre,apellido,edad,obra_social,telefono) VALUES ('Carlos','Gerson',29,'PAMI','2972321459')")
            conn.commit()
            return cursor.lastrowid
    
    
    def test_registrar_paciente(self,conn):
        
        
        db_conn = DBConn("test_config.ini")
        dao = PacienteDAO(db_conn)
        
        dao.registrar_paciente
        
    
    
    
    #Testea que el dao_mostrarpaciente_por_id devuelva la tupla con los datos que lleva un paciente.
    def test_mostrar_paciente_por_id_devuelve_datos(self,conn):
        
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO test_turnos.paciente (nombre,apellido,edad,obra_social,telefono) VALUES ('Carlos','Gerson',29,'PAMI','2972321459')")
            conn.commit()
            
            id_paciente = cursor.lastrowid
        db_conn=DBConn("test_config.ini")
        dao = PacienteDAO(db_conn)
        paciente_test = dao.mostrar_paciente_por_id(id_paciente)
        
        #paciente_test_select = Paciente(id_paciente=id_paciente_test[0],nombre=id_paciente_test[1],apellido=id_paciente_test[2],edad=id_paciente_test[3],obra_social=id_paciente_test[4],telefono=id_paciente_test[5])
        
        
        assert paciente_test is not None
        assert isinstance(paciente_test , tuple)
        assert paciente_test[0]  == id_paciente
        assert paciente_test[1] == 'Carlos'
        assert paciente_test[2] == 'Gerson'
        assert paciente_test[3] == 29
        assert paciente_test[4] == 'PAMI'
        assert paciente_test[5] == '2972321459'
