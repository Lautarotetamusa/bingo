from src.carton import intentoCarton
from src.bingo import mostrar
from src.tests import ord_filas

def test_ord_filas():
    mi_carton = intentoCarton()
    mostrar(mi_carton)
    assert ord_filas(mi_carton)
