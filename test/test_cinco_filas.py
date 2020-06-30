from src.carton import carton_valido
from src.tests import cinco_celdas


def test_cinco_celdas():
    mi_carton = carton_valido()
    assert cinco_celdas(mi_carton)
