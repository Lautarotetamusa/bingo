from bingo import columna

def ord_filas(carton):
    for j in range(0, 3):
        for i in range(0, 8):
            if carton[j][i+1] != 0:
                if carton[j][i] > carton[j][i+1]:
				    return False

    return True

#----------------

def no_repetir_num(carton):
    fil = 3
    col = 9

    for i in range (0, fil):
        for j in range(0, col):
            for ii in range (i, fil):
                for jj in range(j, col):
                    if carton[i][j] != 0 and i != ii and j != jj:
                        if (carton[i][j] == carton[ii][jj]):
							return False

	return True

#------------------

def ocupadas(C):
    ocupadas = 0
    for i in C:
        if i != 0:
            ocupadas += 1

    return ocupadas

def filas_vacias(carton):
    valor_fila = 0
    for fila in carton:
        for celda in fila:
            valor_fila += celda

        if valor_fila <= 0:
			return False

        valor_fila = 0

    return True


def no_dos_vacias(carton):
    for fila in carton:
        for i in range(0, 7):
            if (ocupadas((fila[i], fila[i+1], fila[i+2])) == 0):
				return False

    return True


def no_dos_ocupadas(carton):
    for fila in carton:
        for i in range(0, 7):
            if (ocupadas((fila[i], fila[i+1], fila[i+2])) == 3):
			    return False

    return True
#---------------

#==========funciones auxiliares==========
def vacia(c):
    return (c[0] == 0 and c[1] == 0 and c[2] == 0)

def llena(c):
    return (c[0] != 0 and c[1] != 0 and c[2] != 0)

def cant_celdas(c):
    cant = 0
    for i in c:
        if i != 0:
            cant = cant + 1

    return cant

def decena(col, i):
    c = 0
    for celda in col:
        if celda == 0:
            c = c + 1
        elif celda < 10*(i+1) and celda >= 10*i:
            c = c + 1

    return c == 3
#=======================================

def no_vacias(carton):
    vacias = 0
    for i in range(0, 9):
        if vacia(columna(carton, i)):
	        return False

    return True

def no_3_ocupadas(carton):
    ocupadas = 0
    for i in range(0, 9):
        if llena(columna(carton, i)):
			return False

    return True

def tres_con_una_celda(carton):
    una_celda = 0
    for i in range(0, 9):
        c = columna(carton, i)
        if cant_celdas(c) == 1:
            una_celda = una_celda + 1

    return una_celda == 3

def decena_ordenadas(carton):
    decenasCorrectas = 0
    for i in range(0, 9):
        col = columna(carton, i)
        if decena(col, i) == False:
			return False

    return True

#-----------------

def col_ordenadas(carton):

    colCorrectas = 0
    for i in range(0, 9):
        col = columna(carton, i)
        c = 0

        #contamos cuantas celdas vacias hay
        for j in range(0, 3):
            if col[j] == 0:
                c += 1

        #si la cant de celdas vacias no es 2
        if c != 2:
            if col[1] == 0:             #cuando la 2da casilla esta vacia
                if col[2] > col[0]:
					colCorrectas += 1
            elif col[2] == 0:           #cuando la ultima casilla esta vacia
                if col[1] > col[0]:
					colCorrectas += 1
            else:                       #cuando no hay ninguna vacia
                if (col[2] > col[1] and col[1] > col[0] and col[2] > col[0]):
					colCorrectas += 1
        else:
            colCorrectas += 1

    return colCorrectas == 9

#-----------------


def cinco_celdas(carton):
    cant_celdas = 0
    filasCorrectas = 0
    for fila in carton:
    	for celda in fila:
        	if celda != 0:
        	    cant_celdas += 1

        if cant_celdas != 5:
			return False

    	cant_celdas = 0

    return True
#-----------------

def contar_celdas_ocupadas(carton):

    celdas_ocupadas = 0
    for fila in carton:
		for celda in fila:
		    if celda != 0:
		    	celdas_ocupadas += 1

    return celdas_ocupadas == 15

def columas_vacias(carton):
    for i in range(9):
        if (carton[0][i] + carton[1][i] + carton[2][i]) == 0:
            return False

    return True

#-----------------

def matrix3x9(carton):
    cant_filas = 0
    filasDeNueve = 0
    for fila in carton:
        if len(fila) != 9:
			return False
        cant_filas += 1

    return (cant_filas == 3)

#------------------

def uno_a_noventa(carton):
	for fila in carton:
		for celda in fila:
			if celda < 0 or celda > 90:
				return False

	return True
