def test_no_repetir_num():
    carton = ((11,25,31,45,56,67,78,89,90),
              (10,54,35,87,95,85,99,53,12),
              (14,16,17,18,19,20,22,23,46)
            )
    fil = 3
    col = 9 

    for i in range (0, fil):
        for j in range(0, col):
            for ii in range (i, fil):
                for jj in range(j+1, col):
                    assert carton[i][j] <> carton[ii][jj]

