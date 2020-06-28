
def carton():
    carton = (
	    (1,0,0,1,1,0,1,0,1),
	    (0,1,1,1,0,1,1,1,1),
        (0,1,0,0,1,0,0,1,0)
	)
    return carton

def columna(carton, nro_columna):
    return(
        carton[0][nro_columna],
        carton[1][nro_columna],
        carton[2][nro_columna]
    )

def mostrar(carton):
	for fila in carton:
		print fila
