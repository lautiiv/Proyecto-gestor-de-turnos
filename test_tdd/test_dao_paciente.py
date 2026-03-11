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


def conexion_paciente_dao():
    db_conn = DBConn("test_config.ini")
    dao = PacienteDAO(db_conn)
    return dao

class TestPacienteDao:
    #HELPER crea paciente para las siguientes pruebas
    def crear_paciente(self,conn):
        
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO test_turnos.paciente (nombre,apellido,edad,obra_social,telefono) VALUES ('Carlos','Gerson',29,'PAMI','2972321459')")
            conn.commit()
            return cursor.lastrowid
    
    
    def test_registrar_paciente(self,conn): 
        
        dao = conexion_paciente_dao()
        
        paciente = Paciente("Pedro","Garcia",34,"PAMI","2954332211")
        
        id_paciente = dao.registrar_paciente(paciente)
        
        select_paciente_registrado = dao.mostrar_paciente_por_id(id_paciente)
        
        assert id_paciente > 0
        assert id_paciente is not None
        assert select_paciente_registrado[0] == id_paciente
        assert select_paciente_registrado[1] == paciente.nombre
        assert select_paciente_registrado[2] == paciente.apellido
        assert select_paciente_registrado[3] == paciente.edad
        assert select_paciente_registrado[4] == paciente.obra_social
        assert select_paciente_registrado[5] == paciente.telefono
    
    #Testea que el dao_mostrarpaciente_por_id devuelva la tupla con los datos que lleva un paciente.
    def test_mostrar_paciente_por_id_devuelve_datos(self,conn):

        id_paciente = self.crear_paciente(conn)
        dao = conexion_paciente_dao()
        
        paciente_test = dao.mostrar_paciente_por_id(id_paciente)
        
        
        assert paciente_test is not None
        assert isinstance(paciente_test , tuple)
        assert paciente_test[0]  == id_paciente
        assert paciente_test[1] == 'Carlos'
        assert paciente_test[2] == 'Gerson'
        assert paciente_test[3] == 29
        assert paciente_test[4] == 'PAMI'
        assert paciente_test[5] == '2972321459'

    def test_modificar_paciente(self,conn):

        dao = conexion_paciente_dao()
        
        id_paciente = self.crear_paciente(conn)
        
        paciente_select = dao.mostrar_paciente_por_id(id_paciente)
        
        paciente= Paciente(paciente_select[1],paciente_select[2],paciente_select[3],paciente_select[4],paciente_select[5],paciente_select[0])
        
        paciente.nombre = "Anastacia"
        paciente.apellido = "Perez"
        paciente.edad = 50
        paciente.obra_social = "Sempre"
        paciente.telefono = "0303456"
        
        update = dao.modificar_paciente(paciente)
        
        paciente_test = dao.mostrar_paciente_por_id(id_paciente)
        
        assert update == 1
        assert paciente_test is not None
        assert paciente_test[0] == id_paciente
        assert paciente_test[1] == paciente.nombre
        assert paciente_test[2] == paciente.apellido
        assert paciente_test[3] == paciente.edad
        assert paciente_test[4] == paciente.obra_social
        assert paciente_test[5] == paciente.telefono
    
    def test_borrar_paciente(self,conn):
        
        dao = conexion_paciente_dao()
        
        id_paciente = self.crear_paciente(conn)
        
        existe_paciente = dao.verificar_paciente_existe(id_paciente)
        
        delete_filas_afectadas = dao.eliminar_paciente(id_paciente)
        
        paciente_borrado = dao.verificar_paciente_existe(id_paciente)
        
        assert existe_paciente == True
        assert delete_filas_afectadas == 1
        assert paciente_borrado == False
        

        
    def test_verificar_si_paciente_existe(self,conn):
        
        dao = conexion_paciente_dao()
        id_paciente = self.crear_paciente(conn)
        
        existe_paciente = dao.verificar_paciente_existe(id_paciente)
        
        assert existe_paciente
    
    def test_verificar_paciente_no_existe(self,conn):
        dao = conexion_paciente_dao()
        
        id_cero = dao.verificar_paciente_existe(0)
        id_nuevenueve = dao.verificar_paciente_existe(99)
        id_negativo = dao.verificar_paciente_existe(-1)
        
        assert id_cero is False
        assert id_nuevenueve is False
        assert id_negativo is False
        
    def test_mostrar_paciente_inexistente_por_id(self,conn):
        dao = conexion_paciente_dao()
        
        id_negativo = dao.verificar_paciente_existe(-1)
        id_alto = dao.verificar_paciente_existe(9999)
        id_cero = dao.verificar_paciente_existe(0)
        
        assert id_negativo is False
        assert id_alto is False
        assert id_cero is False
            
    def test_eliminar_paciente_id_erroneo(self,conn):
        dao = conexion_paciente_dao()
        
        id_negativo = dao.eliminar_paciente(-1)
        id_alto = dao.eliminar_paciente(99999)
        id_cero = dao.eliminar_paciente(0)
        
        assert id_negativo == 0
        assert id_alto == 0
        assert id_cero == 0
        
    def test_modificar_paciente_erroneo(self,conn):
        dao = conexion_paciente_dao()
        
        paciente_menos_uno = Paciente("Carlos","Pepito",33,"Pami","29543322",-1)
        paciente_alto = Paciente("Carlos","Pepito",33,"Pami","29543322",99999)
        paciente_cero = Paciente("Carlos","Pepito",33,"Pami","29543322",-1)
        
        id_negativo = dao.modificar_paciente(paciente_menos_uno)
        id_alto = dao.modificar_paciente(paciente_alto)
        id_cero = dao.modificar_paciente(paciente_cero)
        
        assert id_negativo == 0
        assert id_alto == 0
        assert id_cero == 0