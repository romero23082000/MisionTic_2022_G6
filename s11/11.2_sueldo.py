# "Un vendedor recibe un sueldo base, mas un 10% extra por comisión de
# sus ventas, el vendedor desea saber cuanto dinero obtendrá por
# concepto de comisiones por las tres ventas que realiza en el mes y el
# total que recibirá en el mes tomando en cuenta su sueldo base y
# comisiones."

porcentaje_Comision = 0.10
venta1, venta2, venta3 = input(
    "ingrese las ventas separadas por espacio").split()

total_ventas = int(venta1) + int(venta2) + int(venta3)
print(f"el total de ventas es: {total_ventas}")
salario_base = float(input("Ingrese su sueldo base"))
comisiones = total_ventas * porcentaje_Comision
salario_total = salario_base+comisiones

print(f"sus comisiones este mes son:{comisiones}")
print(f"sus salario total este mes es:{salario_total}")
