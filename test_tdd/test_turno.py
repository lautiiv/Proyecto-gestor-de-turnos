import pytest
from dominio.turno import Turno

turno1 = Turno(2,2,2,"1/13/2025","RMN de Cerebro","ocupado")

@pytest.mark.parametrize("actual, esperado",[
    (turno1.id_turno, 2),
    (turno1.id_paciente, 2),
    (turno1.id_resonador, 2),
    (turno1.fecha, "1/13/2025"),
    (turno1.nombre_estudio, "RMN de Cerebro"),
    (turno1.estado_del_turno, "ocupado")
    
])

def test_clase_turno(actual,esperado):
    assert actual == esperado
   
    
turno2 = Turno(1,1,1,"24/12/25","RMN Abdomen","Reservado")

def test_getter_id_turno():
    assert turno2.id_turno == 1
    
def test_getter_id_paciente():
    assert turno2.id_paciente == 1
    
def test_getter_id_resonador():
    assert turno2.id_resonador == 1
    
def test_getter_fecha():
    assert turno2.fecha == "24/12/25"
    
def test_getter_estudio():
    assert turno2.nombre_estudio == "RMN Abdomen"
    
def test_estado_turno_setter():
    assert turno2.estado_del_turno == "Reservado"
    
def test_setter_nombre_estudio():
    turno2.nombre_estudio = "RMN Torax"
    assert turno2.nombre_estudio == "RMN Torax"
    
def test_setter_estado_del_turno():
    turno2.estado_del_turno = "disponible"
    assert turno2.estado_del_turno == "disponible"
