import pytest
from dominio.paciente import Paciente

paciente1 = Paciente(None,"Lautaro","Villafañe",27,"Boreal",2954337927)

@pytest.mark.parametrize("dato,valor_esperado",[
    (paciente1.id_paciente, None),
    (paciente1.nombre,"Lautaro"),
    (paciente1.apellido,"Villafañe"),
    (paciente1.edad, 27),
    (paciente1.obra_social,"Boreal"),
    (paciente1.telefono,2954337927)
    ])


def test_paciente(dato,valor_esperado):
    assert dato == valor_esperado

paciente2 = Paciente(None,"Pedro","Jalisco",99,"Particular",2660303456)
    
def test_setter_nombre():
    paciente2.nombre = "Candela"
    assert paciente2.nombre == "Candela"
    
def test_setter_apellido():
    paciente2.apellido = "Pelegrino"
    assert paciente2.apellido == "Pelegrino"
    
def test_setter_edad():
    paciente2.edad = 26
    assert paciente2.edad == 26
    
def test_setter_obra_social():
    paciente2.obra_social = "MET"
    assert paciente2.obra_social == "MET"
    
def test_setter_telefono():
    paciente2.telefono = 295533333
    assert paciente2.telefono == 295533333