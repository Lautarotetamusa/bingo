from src.bingo import carton_valido
from src.bingo import mostrarCarton
from src.tests import ord_filas

def test_ord_filas():
    mi_carton = carton_valido()
    assert ord_filas(mi_carton)
