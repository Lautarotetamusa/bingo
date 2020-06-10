from src.bingo import columna
carton = ((0,1,3,4,5,0,0,8,9),
          (1,12,0,14,0,6,0,8,0),
          (0,0,22,0,24,0,26,0,28)
         )


def vacia(c):
    return (c[0] == 0 and c[1] == 0 and c[2] == 0)

def llena(c):
    return (c[0] != 0 and c[1] != 0 and c[2] != 0)

def test_no_vacias():
    for i in range(0, 9):
        assert vacia(columna(carton, i)) == False


def test_no_3_ocupadas():
    for i in range(0, 9):
        assert llena(columna(carton, i)) == False
