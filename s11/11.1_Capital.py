# Ejercicio
# Suponga que un individuo desea invertir su capital en el banco
# y desea saber cuanto dinero ganara despues de un mes si el barco
# paga a razon de 15% efectivo anual

INTERES_ANUAL = 0.15
INTERES_MENSUAL = INTERES_ANUAL/12

capital = float(input("Por favor ingrese el capital que desea invertir"))
rendimiento = capital*INTERES_MENSUAL

print(f"Su rendimiento despues de un mes es: {rendimiento:2f}")
