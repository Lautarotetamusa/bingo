def test_ord_filas():
    carton = ((1,2,3,4,5,6,7,8,9,10),
              (11,12,13,14,15,16,17,18,19),
              (20,21,22,23,24,25,26,27,28)
              )
     
    for j in range(0, 3):
        comparar = carton[j][0]
        for i in range(0, 8):
            assert carton[j][i] < carton[j][i+1]
            

    