IGV = 0
monto = 0

precio = int(input("INGRESE PRECIO"))
cant = int(input("INGRESE CANTIDAD"))

monto = (precio * cant)

if (monto > 100):
    IGV = monto * 0.18

print(f"TOTAL : ${monto}")
print(f"IGV 18% : ${IGV}")
print(f"TOTAL A PAGAR : ${(monto + IGV)}")