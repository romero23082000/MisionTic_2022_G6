# "Una tienda ofrece un descuento del 15% sobre el total de la compra y un
# cliente desea saber cuanto deberá pagar finalmente por su compra."

descuento = 0.15

total_compra = float(input("Ingrese el total de la compra"))
descuento_Compra = total_compra * descuento
total_pagar = total_compra - descuento_Compra

print(f"su total a pagar es: {total_pagar}")
