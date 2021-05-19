# Ejercicio 1
# Diseñe un programa que calcule la varianza de cinco numeros depositados en las posiciones de
# memoria que van de la 10 a la 14 y que deje el resultado en la direccion de memoria 15

# Abstraccion
# 1. definir lista con sus terminos del 10 al 14
# 2. Realizar codigo que ejecute la formula del enunciado
# 3. la posicion 15 debe mostrar el resultado de esta formula


# Definir lista
ListaNumeros = [10, 11, 12, 13, 14]


# Proceso que ejecuta toda la formula
SumaParaPromedio = sum(ListaNumeros)
print("La suma de los datos da:", SumaParaPromedio)

CalcularPromedio = int(SumaParaPromedio / 5)
print("El promedio es: ", CalcularPromedio)

EjecutarFormula = int(((ListaNumeros[0]-CalcularPromedio)**2
                       + (ListaNumeros[1]-CalcularPromedio)**2 +
                       (ListaNumeros[2]-CalcularPromedio)**2
                       + (ListaNumeros[3]-CalcularPromedio)**2
                       + (ListaNumeros[4]-CalcularPromedio)**2)/5)

print("La varianza es: ", EjecutarFormula)
# El append esta agregando el resultado de ejecutar la formula al final de la lista
ListaNumeros.append(EjecutarFormula)
print("Es una: ", type(ListaNumeros), "El resultado es:", ListaNumeros)
