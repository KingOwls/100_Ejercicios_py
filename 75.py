

monto = int(input("MONTO DE LA COMPRA"))

if (monto >= 350):
    desct = monto * 0.35
    print(f"DESCUENTO ES DE 35% : ${desct}")
else:
    desct = monto * 0.10
    print(f"DESCUENTO ES DE 10% : ${desct}")

print(f"MONTO A PAGAR : ${monto - desct}")