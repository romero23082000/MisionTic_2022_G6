edad = int(input("ingresa tu edad: "))

if edad >= 18:
    print("puedes entrar al bar")
else:
    tiempo = 18-edad
    print(f"no puedes entrar al bar regresa en {tiempo} años")
