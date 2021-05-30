

numeroComputadores = int(input("inserte el nuermo de computadoras a comprar"))
valorPc = float(3500000)

if(numeroComputadores < 5):
    print("ganaste un 10% de descuento")
    total = valorPc * numeroComputadores
    totalCompra = total - (total * 0.10)
    print("total de tu compra es:", totalCompra)
elif(numeroComputadores >= 5 and numeroComputadores < 10):
    print("tienes un descuento del 20% en tu compra")
    total = valorPc * numeroComputadores
    totalCompra = total - (total * 0.20)
    print("total de tu compra es:", totalCompra)
elif(numeroComputadores > 10):
    print("tienes un descuento del 40% en tu compra")
    total = valorPc * numeroComputadores
    totalCompra = total - (total * 0.40)
    print("total de tu compra es:", totalCompra)
