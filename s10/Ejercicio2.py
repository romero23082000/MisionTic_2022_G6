# Ejercicio 2
# Diseña un programa que calcule la media de cinco numeros depositados en las posiciones de
# memoria que van de la 10 a la 14 y el restultado debe ir en la posicion 15

# Abstraccion
# 1.Realizar la lista
# 2.Solicitar numeros al usuario
# 3.Ejecutar la formula indicada

ListNumeros = []
numero1 = int(input("inserte numero 1: "))
ListNumeros.append(numero1)
numero2 = int(input("inserte numero 2: "))
ListNumeros.append(numero2)
numero3 = int(input("inserte numero 3: "))
ListNumeros.append(numero3)
numero4 = int(input("inserte numero 4: "))
ListNumeros.append(numero4)
numero5 = int(input("inserte numero 5: "))
ListNumeros.append(numero5)
print("Valores agregados a la lista: ", ListNumeros)

mediaAritmetica = sum(ListNumeros)/5
ListNumeros.append(mediaAritmetica)
print("La media aritmetica es: ", mediaAritmetica,
      "y la lista queda asi: ",  ListNumeros)
