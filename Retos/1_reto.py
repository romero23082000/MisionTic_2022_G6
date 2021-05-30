# Pedir datos
salario1, cantHoras1, bonificacion1 = input().split()
# Calculo del valor de la hora
valor_hora = float(float(salario1)/190)

# Proceso de cantidad de horas
if int(cantHoras1) == 0:
    calcHorasExtra = 0
else:
    calcHorasExtra = float((valor_hora * 0.34) + valor_hora)*int(cantHoras1)
#  Proceso de bonificaciones
if int(bonificacion1) == 1:
    calBonificacion = float(float(salario1)*0.061)
else:
    calBonificacion = 0
# Salario total del empleado
salario_total = round(
    float(float(salario1) + calBonificacion + calcHorasExtra), 1)
# Descuentos al salario total
planSalud = float(0.01 * salario_total)
pension = float(0.01 * salario_total)
compensacion = float(0.01 * salario_total)
salarioConDescuento = round(
    salario_total-(compensacion + planSalud + pension), 1)
# Resultados del salario total y del salario con descuento
resultado = print(salario_total, salarioConDescuento)
