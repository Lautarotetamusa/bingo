from src.carton import intentoCarton
from src.bingo import mostrar
from src.tests import no_repetir_num

def test_no_repetir_num():
    mi_carton = intentoCarton()
    mostrar(mi_carton)
    assert no_repetir_num(mi_carton)
