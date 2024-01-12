
totalPagar = 0


for x in range(10):
    cantidad = int(input(f"COMPRA NUMERO {x + 1}, cuanto compro? : "))
    totalPagar += cantidad
descuento = 0
if (totalPagar > 50):
    descuento = totalPagar * 0.07
print("Consumo total:")
print({totalPagar})
print("Descuento: ")
print({round(descuento, 1)})
print("Total a Pagar: $")
print({totalPagar - descuento})