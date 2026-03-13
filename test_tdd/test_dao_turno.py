import pytest
import mysql.connector
from db.db_conn import DBConn
import datetime

from dao.turno_dao import TurnoDAO
from dominio.turno import Turno

from mysql.connector import errorcode

@pytest.fixture(scope="module")
def conn():
    db_conn = DBConn("test_config.ini")
    conn = db_conn.connect_to_mysql()
    
    try:
        with conn.cursor() as cursor:
            
            cursor.execute("CREATE DATABASE IF NOT EXISTS test_turnos")
            cursor.execute("USE test_turnos")
            
            cursor.execute('''CREATE TABLE IF NOT EXISTS test_turnos.paciente (id_paciente int primary key not null auto_increment,nombre varchar(50) not null,
                           apellido varchar(50) not null
                           , edad int not null
                           , obra_social varchar(50) not null,
                           telefono varchar(20) not null)
                           ''')
            
            query_turno = """
                            CREATE TABLE test_turnos.turno (
                            id_turno INT NOT NULL AUTO_INCREMENT,
                            id_paciente INT NOT NULL,
                            id_resonador INT NOT NULL,
                            fecha DATETIME DEFAULT NULL,
                            nombre_estudio VARCHAR(50) DEFAULT NULL,
                            estado VARCHAR(10) DEFAULT NULL,
                            PRIMARY KEY (id_turno),
                            KEY fk_turno_paciente (id_paciente),
                            KEY fk_turno_resonador (id_resonador),
                            CONSTRAINT fk_turno_paciente 
                            FOREIGN KEY (id_paciente) REFERENCES paciente (id_paciente),
                            CONSTRAINT fk_turno_resonador 
                            FOREIGN KEY (id_resonador) REFERENCES resonador (id_resonador)
                            );
                         """
            query_resonador = """
                                CREATE TABLE test_turnos.resonador (
                                id_resonador INT NOT NULL AUTO_INCREMENT,
                                nombre_equipo VARCHAR(50) DEFAULT NULL,
                                PRIMARY KEY (id_resonador));"""
                                
            cursor.execute(query_resonador)
            cursor.execute(query_turno)
            cursor.execute("DELETE FROM test_turnos.paciente")
            cursor.execute("DELETE FROM test_turnos.resonador ")
            cursor.execute("DELETE FROM test_turnos.turno ")
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

def conexion_turno_dao():
    db_conn = DBConn("test_config.ini")
    dao = TurnoDAO(db_conn)
    return dao

class TestPacienteDao:
    #HELPER paciente
    fecha_str = '2026-03-01 08:00:00'
    FECHA = datetime.datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
    
    def crear_paciente(self,conn):
        
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO test_turnos.paciente (nombre,apellido,edad,obra_social,telefono) VALUES ('Carlos','Gerson',29,'PAMI','2972321459')")
            conn.commit()
            id_paciente = cursor.lastrowid
            return id_paciente    
    #HELEPER resonador
    def crear_resonador(self,conn):
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO test_turnos.resonador (nombre_equipo) VALUES ('3T')")
            conn.commit()
            id_resonador = cursor.lastrowid
            return id_resonador
    #HELPER turno
    def crear_turno(self,conn,id_paciente,id_resonador):
        with conn.cursor() as cursor: 
            cursor.execute("INSERT INTO test_turnos.turno (id_paciente,id_resonador,fecha,nombre_estudio,estado) VALUES (%s,%s,'2026-03-01 08:00:00','RM codo','activo')",(id_paciente,id_resonador))
            conn.commit()
            return cursor.lastrowid
        
    #HELPER QUE INCLUYE LOS 3 HELPERS PACIENTE,RESONADOR Y TURNO.
    def crear_turno_completo(self,conn) -> int:
        id_paciente = self.crear_paciente(conn)
        id_resonador = self.crear_resonador(conn)
        id_turno = self.crear_turno(conn,id_paciente,id_resonador)
        
        return id_turno

    def test_registrar_turno(self, conn):
        dao = conexion_turno_dao()
        id_paciente = self.crear_paciente(conn)
        id_resonador = self.crear_resonador(conn)
        
        fecha_str = '2026-03-01 08:00:00'
        fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
        id_turno = None
        
        turno = Turno(id_turno,id_paciente,id_resonador,fecha,'rm codo','activo')
        id_turno = dao.registrar_turno(turno)
        
        select = dao.informacion_turno_por_id_turno(id_turno)
        
        assert id_turno > 0
        assert select[0] == 'Carlos'
        assert select[1] == 'Gerson'
        assert select[2] == 'rm codo'
        assert select[3] == fecha
        assert select[4] == "3T"
    
    def test_verificar_turno_ocupado(self, conn):
        #Testea el metodo verificar_disponibilidad_horario_dao que devuelve TRUE si hay un turno registrado en ese horario y resonador.
        dao = conexion_turno_dao()
        id_paciente = self.crear_paciente(conn)
        id_resonador = self.crear_resonador(conn)
        
        id_turno = None
        turno = Turno(id_turno,id_paciente,id_resonador, self.FECHA,'RM Mamaria', 'Activo')
        
        dao.registrar_turno(turno)
        existe_turno = dao.verificar_disponibilidad_horario_dao(turno.fecha_hora,id_resonador)
        
        assert existe_turno is True

    def test_verificar_turno_disponible(self,conn):
        #Testea que no haya un turno registrado en ese horario y resonador. Esperamos que este el turno libre en este caso. 
        dao = conexion_turno_dao()
        id_resonador = self.crear_resonador(conn)
        
        turno_ocupado = dao.verificar_disponibilidad_horario_dao(self.FECHA, id_resonador)
        
        assert turno_ocupado is False
        
        
    def test_informacion_turno_por_id_turno(self,conn):
        dao = conexion_turno_dao()
        
        id_turno = self.crear_turno_completo(conn)
        
        info_turno = dao.informacion_turno_por_id_turno(id_turno)
        
        assert id_turno > 0
        assert info_turno[0] == 'Carlos'
        assert info_turno[1] == 'Gerson'
        assert info_turno[2] == 'RM codo'
        assert info_turno[3] == self.FECHA
        assert info_turno[4] == "3T"
        
    def test_informacion_turno_por_id_paciente(self,conn):
        dao = conexion_turno_dao()
        
        id_paciente = self.crear_paciente(conn)
        id_resonador = self.crear_resonador(conn)
        #id_turno,id_paciente,id_resonador,fecha_hora: datetime,nombre_estudio,estado

        #datos necesarios para crear instancia turno
        id_turno = None
        fecha_str_1 = '2026-03-01 09:00:00'
        fecha_str_2 = '2026-03-01 10:00:00'
        
        fecha_turno_1 = datetime.datetime.strptime(fecha_str_1, "%Y-%m-%d %H:%M:%S")
        fecha_turno_2 = datetime.datetime.strptime(fecha_str_2, "%Y-%m-%d %H:%M:%S")
        
        turno_1 = self.crear_turno(conn,id_paciente,id_resonador)
        turno_2 = Turno(id_turno,id_paciente,id_resonador,fecha_turno_1,'RM abdomen','activo')
        turno_3 = Turno(id_turno,id_paciente,id_resonador,fecha_turno_2,'RM pelvis','activo')
        
        turno_bdd_2 = dao.registrar_turno(turno_2)
        turno_bdd_3 = dao.registrar_turno(turno_3)
        
        turnos = dao.informacion_turno_por_id_paciente(id_paciente)
        
        assert len(turnos) == 3
        #Paciente 1
        assert turnos[0][0] == 'RM codo'
        assert turnos[0][1] == self.FECHA
        assert turnos[0][2] == '3T'
        #Paciente 2
        assert turnos[1][0] == turno_2.nombre_estudio
        assert turnos[1][1] == fecha_turno_1
        assert turnos[1][2] == '3T'
        #Paciente 3
        assert turnos[2][0] == turno_3.nombre_estudio
        assert turnos[2][1] == fecha_turno_2
        assert turnos[2][2] == '3T'
        
    def test_informacion_turno_id_paciente_sin_turnos(self,conn):
        #Verifica que al insertar un id_paciente sin turnos asignados devuelva una lista vacia
        id_paciente = self.crear_paciente(conn)
        dao = conexion_turno_dao()
        
        turnos = dao.informacion_turno_por_id_paciente(id_paciente)
        assert turnos == []
        
    def test_inf_turno_id_paciente_id_erroneo(self,conn):
        dao = conexion_turno_dao()
        
        turnos = dao.informacion_turno_por_id_paciente(999)
        
        assert len(turnos) == 0
        assert turnos == []
        
    def test_modificar_estado(self,conn):
        #Modifica el estado del turno y devuelve 1 si alguna linea fue afectada
        id_paciente = self.crear_paciente(conn)
        id_resonador = self.crear_resonador(conn)
        id_turno = self.crear_turno(conn,id_paciente,id_resonador)
        #el estado del turno es activo
        
        dao = conexion_turno_dao()
        
        turno_modificado = dao.modificar_estado_turno_dao(id_turno,"cancelado")
        
        assert turno_modificado > 0
    
    def test_modificar_estado_erroneo(self,conn):
        #intenta modificar un turno con id_erroneo
        
        dao = conexion_turno_dao()
        
        turno_modificado = dao.modificar_estado_turno_dao(9129,"activo")
        
        assert turno_modificado == 0
        
    def test_modificar_estado_con_mismo_estado(self,conn):
        #intenta modificar un estado con el mismo estado que ya tenia asignado. Antes: activo, despues: activo.
        
        dao = conexion_turno_dao()
        id_paciente = self.crear_paciente(conn)
        id_resonador = self.crear_resonador(conn)
        id_turno = self.crear_turno(conn,id_paciente,id_resonador)
        #estado activo
        
        turno_modificado = dao.modificar_estado_turno_dao(id_turno,'activo')
        
        assert turno_modificado == 0