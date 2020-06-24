from src.carton import intentoCarton
from test.tests import uno_a_noventa

def test_uno_a_noventa():

    assert uno_a_noventa(intentoCarton()) == True
