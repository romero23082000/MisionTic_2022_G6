multiplo = int(input("digite un numero entero: "))
print(f"los multiplos de {multiplo} son: ")

if multiplo % 3 == 0 and multiplo % 5 == 0:
    print("Es multiplo de 3 y de 5")
elif multiplo % 3 == 0:
    print("Es multiplo de 3")
elif multiplo % 5 == 0:
    print("Es multiplo de 5")
else:
    print("no es un multiplo")
