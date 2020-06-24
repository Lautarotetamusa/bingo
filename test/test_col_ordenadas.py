from test.tests import col_ordenadas
from src.carton import intentoCarton
from src.bingo import mostrar

def test_col_ordenadas():
    carton = intentoCarton()
    mostrar(carton)
    assert col_ordenadas(carton)
