from src.bingo import carton

def test_uno_a_noventa():
    mi_carton = ((3,5,62,5,1,74,14,5,2),
                 (56,1,4,15,23,41,7,2,5),
                 (6,12,5,1,75,31,41,64,51)
                )
    contador = 0
            
    for fila in range(0, 3):
        for columna in range (0, 9):
            celda = mi_carton[fila][columna]
            assert celda >= 1 and celda <= 90
