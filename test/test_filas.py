from src.bingo import carton

def test_filas_vacias():
    mi_carton = carton()
    valor_fila = 0
    for fila in mi_carton:
        for celda in fila:
            valor_fila += celda

        assert valor_fila > 0

    valor_fila = 0


carton_falla = (
            (1,0,1,0,1,0,1,0,1),
            (0,1,1,0,0,1,0,1,1),
            (0,1,0,1,1,0,0,1,0)
        )


def test_no_dos_vacias():
    mi_carton = carton()
    for fila in mi_carton:
        for i in range(0, 7):
            assert (fila[i] + fila[i+1] + fila[i+2]) != 0


def ocupadas(C):
    ocupadas = 0
    for i in C:
        if i != 0:
            ocupadas += 1

    return ocupadas

def test_no_dos_ocupadas():
    mi_carton = carton()
    for fila in carton_falla:
        for i in range(0, 7):
            assert ocupadas((fila[i], fila[i+1], fila[i+2])) < 3

