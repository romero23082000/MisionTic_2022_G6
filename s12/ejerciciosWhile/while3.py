MAXIMOS_INTENTOS = 3
password = "1234"
contador = 0

intento = input("Ingrese su contraseña: ")

if intento == password:
    print("Trasaccioín existosa")
else:
    while(contador < MAXIMOS_INTENTOS):
        intento = input("Ingrese su contraseña: ")
        if intento == password:
            print("Trasaccíon existosa")
            break
        contador += 1
print(contador)
print("bloqueo su cuenta")
