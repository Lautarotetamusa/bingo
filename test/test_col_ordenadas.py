def test_col_ordenadas():
    carton = ((1,2,3,4,5,6,7,8,9,10),
              (11,12,13,14,15,16,17,18,19),
              (20,21,22,23,24,25,26,27,28)
              )

    for i in range(0, 9):
        assert carton[1][i] < carton [2][i] and carton[0][i] < carton[1][i] 