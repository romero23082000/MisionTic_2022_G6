inversion = float(input("Por favor ingrese el capital que deseas invertir: "))
porcentaje_intereses = float(input("Ingrese el porcentaje de interes: "))
total = inversion * porcentaje_intereses

if total > 7000:
    total_final = inversion + total
    print(f"este es su capital final {total_final}")

print(f"Este es su capital..{inversion}")
