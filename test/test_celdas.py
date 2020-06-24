from src.carton import intentoCarton
from test.tests import columas_vacias
from test.tests import contar_celdas_ocupadas

def test_contar_celdas_ocupadas():
    mi_carton = intentoCarton()
    assert contar_celdas_ocupadas(mi_carton)



def test_columas_vacias():
    mi_carton = intentoCarton()
    assert columas_vacias(mi_carton)
