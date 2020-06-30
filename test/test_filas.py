from src.bingo import carton_valido

from src.tests import no_dos_ocupadas
from src.tests import no_dos_vacias
from src.tests import filas_vacias

mi_carton = carton_valido()

def test_filas_vacias():
    assert filas_vacias(mi_carton)

def test_no_dos_vacias():
    assert no_dos_vacias(mi_carton)

def test_no_dos_ocupadas():
    assert no_dos_ocupadas(mi_carton)
