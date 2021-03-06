from src.bingo import carton_valido

from src.tests import decena_ordenadas
from src.tests import tres_con_una_celda
from src.tests import no_3_ocupadas
from src.tests import no_vacias

carton = carton_valido()

def test_no_vacias():
    assert no_vacias(carton)


def test_no_3_ocupadas():
    assert no_3_ocupadas(carton)


def test_tres_con_una_celda():
    assert tres_con_una_celda(carton)


def test_decena_ordenadas():
    assert decena_ordenadas(carton)
