# Ejercicios
# Ejercicio NUMERO 1
print("por favor ingrese cuatro numero flotantes o decimales")
flotante1 = float(input("por favor ingrese flotante numero 1--:"))
flotante2 = float(input("por favor ingrese flotante numero 1--:"))
flotante3 = float(input("por favor ingrese flotante numero 1--:"))
flotante4 = float(input("por favor ingrese flotante numero 1--:"))
# Operaciones basicas
suma = flotante1 + flotante2 + flotante3 + flotante4
resta = flotante1 - flotante2 - flotante3 - flotante4
multiplicacion = flotante1 * flotante2 * flotante3 * flotante4
division = round(flotante1 / flotante2 / flotante3 / flotante4, 3)
# Modulos o porcentajes
modulo1 = round(flotante1 % flotante2, 3)
modulo2 = round(flotante3 % flotante4, 3)
# Potenciacion
potencia1 = pow(flotante2, flotante4)
potencia2 = pow(flotante3, flotante4)
# Muestra resultados
print('Resultado de la suma--:' + str(suma))
print('Resultado de la suma--:' + str(resta))
print('Resultado de la multiplicacion--:' + str(multiplicacion))
print('Resultado de la division--:' + str(division))
print(modulo1)
print(modulo2)
print(potencia1)
print(potencia2)

# EJERCICIO NUMERO 2
print("VAMOS A VENDER UN COMPUTADOR")
precio = float(input('por favor inserte valor del computador $'))
bonus = precio * 0.30
total = precio + bonus
print('el precio del computador es:', precio,
      'y con el 30 por ciento de aumento el equipo vale: ', bonus, ' y su total es: ', total)

# EJERCICIO NUMERO 3
hora = int(input("ingrese por favor un numero de horas-:"))
CantMinutos = hora * 60
CantSeg = hora * 3600
div = int(hora / 24)

if hora > 24 or hora == 24:
    muldias = int(div * 24)
    resta = hora - muldias
    print('Su hora ingresada fue:', hora, 'la cantidad de minutos es : ', CantMinutos,
          'la cantidad de segundos es :', CantSeg, " y te refieres a ", div, "dias y",  resta, "horas")
else:
    print('Su hora ingresada fue:', hora, 'la cantidad de minutos es : ', CantMinutos,
          'la cantidad de segundos es :', CantSeg, " y te refieres a ", div, "dias y",  hora, "horas")
