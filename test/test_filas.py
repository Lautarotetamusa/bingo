from src.bingo import carton


def test_filas_vacias():
    mi_carton = carton()
    valor_fila = 0
    for fila in mi_carton:
        for celda in fila:
            valor_fila += celda

        assert valor_fila > 0

        valor_fila = 0
