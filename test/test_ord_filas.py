from src.carton import carton_valido
from src.bingo import mostrar
from src.tests import ord_filas

def test_ord_filas():
    mi_carton = carton_valido()
    mostrar(mi_carton)
    assert ord_filas(mi_carton)
