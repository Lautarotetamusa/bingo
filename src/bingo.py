
def carton():
    carton = (
	    (1,0,0,1,1,0,1,0,1),
	    (0,1,1,1,0,1,1,1,1),
            (0,1,0,0,1,0,0,1,0) 
	)
    return carton


def carton_test_filas_vacias():
    carton = (
            (1,1,1,1,1,1,1,0,1),
            (0,0,0,0,0,0,0,0,0),
            (1,1,1,1,1,1,0,1,0)
            )
    return carton


print(carton())


