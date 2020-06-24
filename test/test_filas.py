from src.carton import intentoCarton
from src.bingo import mostrar

from test.tests import no_dos_ocupadas
from test.tests import no_dos_vacias
from test.tests import filas_vacias

def test_filas_vacias():
    mi_carton = intentoCarton()
    mostrar(mi_carton)
    assert filas_vacias(mi_carton)

def test_no_dos_vacias():
    mi_carton = intentoCarton()
    mostrar(mi_carton)
    assert no_dos_vacias(mi_carton)

def test_no_dos_ocupadas():
    mi_carton = intentoCarton()
    mostrar(mi_carton)
    assert no_dos_ocupadas(mi_carton)
