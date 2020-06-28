from src.carton import intentoCarton
from src.tests import cinco_celdas


def test_cinco_celdas():
    mi_carton = intentoCarton()
    assert cinco_celdas(mi_carton)
