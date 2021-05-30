from random import choice
BLANCA = 0
VERDE = 0.10
AMARILLA = 0.25
AZUL = 0.50
ROJA = 1


bolita = [BLANCA, VERDE, ROJA, AZUL, AMARILLA]
color_bolita = choice(bolita)
compra = float(input("ingrese el precio del producto"))

if(color_bolita == BLANCA):
    print("lo siento no ganaste descuento en tu compra")
elif(color_bolita == VERDE):
    print("tienes un descuento del 10% en tu compra")
    valor_total = compra - (compra * VERDE)
    print("tu compra bajo a: ", valor_total)
elif(color_bolita == AMARILLA):
    print("tienes un descuento del 25% en tu compra")
    valor_total = compra - (compra * AMARILLA)
    print("tu compra bajo a: ", valor_total)
elif(color_bolita == AZUL):
    print("tienes un descuento del 50% en tu compra")
    valor_total = compra - (compra * AZUL)
    print("tu compra bajo a: ", valor_total)
elif(color_bolita == ROJA):
    print("tienes un descuento del 100% en tu compra")
    valor_total = compra - (compra * ROJA)
    print("tu compra bajo a: ", valor_total)
