from tests import *
import random
import math

def mostrarCarton(carton):
	for fila in carton:
		print fila

def intentoCarton():

    contador = 0
    carton = (
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    )
    numerosCarton = 0

    while (numerosCarton < 15):
      contador = contador + 1
      if (contador == 50):
        return intentoCarton()

      numero = random.randint(1,90)
      columna = int(math.floor(numero / 10))

      if (columna == 9):
          columna = 8

      huecos = 0

      for i in range(3):
        if (carton[i][columna] == 0):
          huecos = huecos + 1

        if (carton[i][columna] == numero):
          huecos = 0
          break

      if (huecos < 2):
        continue

      fila = 0

      for j in range(3):
        huecos = 0
        for i in range(9):
          if (carton[fila][i] == 0):
              huecos = huecos + 1

        if (huecos < 5 or carton[fila][columna] != 0):
          fila = fila + 1
        else:
          break

      if (fila == 3):
        continue

      carton[fila][columna] = numero
      numerosCarton = numerosCarton + 1
      contador = 0

    for x in range(9):
      huecos = 0
      for y in range(3):
        if (carton[y][x] == 0):
            huecos = huecos + 1

      if (huecos == 3):
        return intentoCarton()

    return carton

def testCarton(carton):
	if(ord_filas(carton)
	and no_repetir_num(carton)
	and filas_vacias(carton)
	and no_dos_vacias(carton)
	and no_dos_ocupadas(carton)
	and no_vacias(carton)
	and no_3_ocupadas(carton)
	and tres_con_una_celda(carton)
	and decena_ordenadas(carton)
	and col_ordenadas(carton)
	and cinco_celdas(carton)
	and contar_celdas_ocupadas(carton)
	and columas_vacias(carton)
	and matrix3x9(carton)
	and uno_a_noventa(carton)):
		return True
	return False

def carton_valido():

	intentos = 0

	while True:
		carton = intentoCarton()
		if testCarton(carton):
			return carton
		intentos += 1

mostrarCarton(carton_valido())
