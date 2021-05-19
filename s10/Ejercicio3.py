# 1.Calcular area de un circulo

# Radio = int(input("inserte el radio del circulo: "))
# ElevarRadio = Radio**2
# pi = 3.14
# CalcularRadio = pi*ElevarRadio
# print("El area del circulo es: ", CalcularRadio)


precio = float(input("Inserte el precio del producto sin IVA: "))
precioTotal = precio * 0.16
IvaTotal = int(precio + precioTotal)
print("El precio del producto es: ", precio, " Su precio total con IVA es: ", IvaTotal,
      "y su IVA es: ", precioTotal)
