import pytest
import mysql.connector
from db.db_conn import DBConn
from dao.interfaz_dao.interfaz_paciente_dao import PacienteDAOInterfaz
from dominio.paciente import Paciente
from mysql.connector import errorcode

