from src.bingo import carton

def test_contar_celdas_ocupadas():
	mi_carton = carton()
	celdas_ocupadas = 0
	for fila in mi_carton:
		for celda in fila:
			celdas_ocupadas += celda
	
	assert celdas_ocupadas == 15
