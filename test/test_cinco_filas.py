from src.carton import intentoCarton
from test.tests import cinco_celdas


def test_cinco_celdas():
    mi_carton = intentoCarton()
    assert cinco_celdas(mi_carton)
