from src.bingo import columna
carton = ((0,1,3,4,5,0,0,8,9),
          (1,12,0,14,0,6,0,8,0),
          (0,0,22,0,24,0,26,0,28)
         )


carton_test_tres = ((0,1,3,4,5,4,0,8,9),
                    (1,2,0,4,0,6,0,8,0),
                    (0,0,2,0,0,0,6,0,8)
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
    cont = 0
    for i in range(0, 9):
        c = columna(carton_test_tres, i)
        if cant_celdas(c) == 1:
            cont = cont + 1

    assert cont == 3
