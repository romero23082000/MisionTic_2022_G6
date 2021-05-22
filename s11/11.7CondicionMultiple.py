numero1, numero2 = input(
    "inserte por favor dos numeros separado por espacio").split()

numero1 = int(numero1)
numero2 = int(numero2)

if numero1 > numero2:
    print(f"el numero 1 {numero1} es mayor que el numero 2 {numero2}")
else:
    print(f"el numero 2 {numero2} es mayor que el numero 1 {numero1}")
