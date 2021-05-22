

salario_base = float(input("ingrese su salario:"))
print("Ingrese sus horas extra. Coloque 0 si no tuvo horas extra: ")
cantidad_horas = int(input("ingrese el numero de horas extra"))
print("Coloque 1 si tuvo bonificaciones. Coloque 0 si no tuvo bonificaciones: ")
bonificaciones = int(input("notificaciones"))

valor_hora = float(salario_base/190)


if cantidad_horas == 0:
    calcHorasExtra = 0
else:
    calcHorasExtra = float((valor_hora * 0.34) + valor_hora)*cantidad_horas

if bonificaciones == 1:
    calBonificacion = float(salario_base*0.061)
else:
    calBonificacion = 0

salario_total = round(
    float(salario_base + calBonificacion + calcHorasExtra), 1)

planSalud = float(0.01 * salario_total)
pension = float(0.01 * salario_total)
compensacion = float(0.01 * salario_total)
salarioConDescuento = round(
    salario_total-(compensacion + planSalud + pension), 1)


print(salario_total, salarioConDescuento)
