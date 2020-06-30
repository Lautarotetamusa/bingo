from src.carton import carton_valido
from src.tests  import matrix3x9

def test_matrix3x9():

    assert matrix3x9(carton_valido()) == True
