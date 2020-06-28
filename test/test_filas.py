from src.carton import intentoCarton
from src.bingo import mostrar

from src.tests import no_dos_ocupadas
from src.tests import no_dos_vacias
from src.tests import filas_vacias

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
