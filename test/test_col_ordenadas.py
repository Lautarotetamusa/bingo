from src.tests import col_ordenadas
from src.carton import carton_valido
from src.bingo import mostrar

def test_col_ordenadas():
    carton = carton_valido()
    mostrar(carton)
    assert col_ordenadas(carton)
