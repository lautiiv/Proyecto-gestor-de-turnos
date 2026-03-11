import pytest
import mysql.connector
from db.db_conn import DBConn

from dao.turno_dao import TurnoDAO
from dominio.turno import Turno

from mysql.connector import errorcode

