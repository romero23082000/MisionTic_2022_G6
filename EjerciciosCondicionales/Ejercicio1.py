
ValorPorHora = float(input("Inserte la cantidad de dinero"))

NumHoras = int(input("Inserte el numero de horas extras"))

calHoraXHora = ValorPorHora * NumHoras

if NumHoras >= 40 and NumHoras <= 47:
    horasExtra = NumHoras - 40
    ValorDoble = ValorPorHora * 2
    CalHorasExtra = horasExtra * ValorDoble
    print(CalHorasExtra + calHoraXHora)


if (NumHoras >= 48):
    horasExtra = NumHoras - 40
    ValorDoble = ValorPorHora * 3
    CalHorasExtra = horasExtra * ValorDoble
    print(CalHorasExtra + calHoraXHora)
else:
    print(0)
