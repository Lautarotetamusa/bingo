from src.bingo import columna
carton = ((0,1,3,4,5,0,0,8,9,0),
          (1,12,13,14,15,16,17,18,19),
          (0,21,22,23,24,25,26,27,28)
         )


def vacia(c):
    return (c[0] == 0 and c[1] == 0 and c[2] == 0)

def test_no_vacias():
    for i in range(0, 9):
        assert vacia(columna(carton, i)) == False
