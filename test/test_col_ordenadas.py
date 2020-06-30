from src.tests import col_ordenadas
from src.bingo import carton_valido

def test_col_ordenadas():
    carton = carton_valido()
    assert col_ordenadas(carton)
