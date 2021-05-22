suma = 0

mensaje = ("por favor ingrese los numeros\n"
           "si el numero es igual a 0 para el ciclo")


numeros = int(input(mensaje))

while numeros != 0:
    suma = suma + numeros
    numeros = int(input(mensaje))


print(" la suma de los numeros es: ", suma)
