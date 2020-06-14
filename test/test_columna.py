from src.bingo import columna
carton = ((0,1,3,4,5,0,0,8,9),
          (1,12,0,14,0,6,0,8,0),
          (0,0,22,0,24,0,26,0,28)
         )


carton3 = ((0,1,3,4,5,4,0,8,9),
           (1,2,0,4,0,6,0,8,0),
           (0,0,2,0,0,0,6,0,8)
          )

carton4 = ((0,10,20,30,40,50,60,70,80),
           (2,11,21,31,41,51,61,71,81),
           (9,19,29,39,49,59,69,79,89)
          )




def vacia(c):
    return (c[0] == 0 and c[1] == 0 and c[2] == 0)

def llena(c):
    return (c[0] != 0 and c[1] != 0 and c[2] != 0)

def cant_celdas(c):
    cant = 0
    for i in c:
        if i != 0:
            cant = cant + 1

    return cant

def test_no_vacias():
    for i in range(0, 9):
        assert vacia(columna(carton, i)) == False


def test_no_3_ocupadas():
    for i in range(0, 9):
        assert llena(columna(carton, i)) == False


def test_tres_con_una_celda():
    una_celda = 0
    for i in range(0, 9):
        c = columna(carton3, i)
        if cant_celdas(c) == 1:
            una_celda = una_celda + 1

    assert una_celda == 3

def decena(col, i):
    c = 0
    for celda in col:
        if celda == 0:
            c = c + 1
        elif celda < 10*(i+1) and celda >= 10*i:
            c = c + 1

    return c == 3

def test_decena_ordenadas():
    for i in range(0, 9):
        col = columna(carton4, i)
        assert decena(col, i)
            
