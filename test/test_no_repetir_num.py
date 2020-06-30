from src.bingo import carton_valido
from src.tests import no_repetir_num

def test_no_repetir_num():
    mi_carton = carton_valido()
    assert no_repetir_num(mi_carton)
