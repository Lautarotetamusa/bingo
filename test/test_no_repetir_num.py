from src.carton import carton_valido
from src.bingo import mostrar
from src.tests import no_repetir_num

def test_no_repetir_num():
    mi_carton = carton_valido()
    mostrar(mi_carton)
    assert no_repetir_num(mi_carton)
