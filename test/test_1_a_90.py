from src.bingo import carton_valido
from src.tests import uno_a_noventa

def test_uno_a_noventa():

    assert uno_a_noventa(carton_valido()) == True
