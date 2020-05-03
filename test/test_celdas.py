from src.bingo import carton

def test_contar_celdas_ocupadas():
    mi_carton = carton()
    celdas_ocupadas = 0
    for fila in mi_carton:
	for celda in fila:
	    celdas_ocupadas += celda
	
    assert celdas_ocupadas == 15



def test_columas_vacias():
    contador = 0
    mi_carton = carton()
    cant_columnas = 9

    for i in range(cant_columnas):
        if (mi_carton[0][i] + mi_carton[1][i] + mi_carton[2][i]) >= 1:
            contador += 1
            
    assert contador == cant_columnas
        
