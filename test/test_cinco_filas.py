from src.bingo import carton

carton2 = ((1, 2, 3, 4 ,5, 0, 0, 0, 0),
           (1, 2, 3, 4 ,5, 0, 0, 0, 0),
           (1, 2, 3, 4 ,5, 0, 0, 0, 0)
          )

def test_cinco_celdas():
    mycarton = carton()
    cant_celdas = 0
    for fila in carton2:
        for celda in fila:
            if celda != 0:
                cant_celdas += 1

        assert cant_celdas == 5
        cant_celdas = 0


