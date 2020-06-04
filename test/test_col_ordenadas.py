from src.bingo import columna

def test_col_ordenadas():
    carton = ((2,2,3,4,5,6,7,8,9,10),
              (0,12,13,14,15,16,17,18,19),
              (0,21,22,23,24,25,26,27,28)
              )

    for i in range(0, 9):
        col = columna(carton, i)
        c = 0
        
        #contamos cuantas celdas vacias hay
        for j in range(0, 3):
            if col[j] == 0:
                c += 1
    
        #si la cant de celdas vacias no es 2
        if c != 2:    
            if col[1] == 0:             #cuando la 2da casilla esta vacia
                assert col[2] > col[0]
            elif col[2] == 0:           #cuando la ultima casilla esta vacia
                assert col[1] > col[0]
            else:                       #cuando no hay ninguna vacia
                assert col[2] > col[1] and col[1] > col[0] and col[2] > col[0]
        else:
            assert True
