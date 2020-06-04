carton =   ((5,1,2,3,5,1,6,1,6),
            (6,1,3,6,8,6,1,2,5),
            (9,8,6,1,4,6,8,2,5)
           )


def test_matrix3x9():
    
    cant_filas = 0
    for fila in carton:
        assert len(fila) == 9
        cant_filas += 1

    assert cant_filas == 3
