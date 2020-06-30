from src.bingo import carton_valido
from src.tests import columas_vacias
from src.tests import contar_celdas_ocupadas

def test_contar_celdas_ocupadas():
    mi_carton = carton_valido()
    assert contar_celdas_ocupadas(mi_carton)



def test_columas_vacias():
    mi_carton = carton_valido()
    assert columas_vacias(mi_carton)
