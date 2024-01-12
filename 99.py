cantidad = float(input("INGRESE CANTIDAD A COMPRAR"))

if (cantidad >= 1 and cantidad <= 3):
    costo = float(15)
elif (cantidad >= 4 and cantidad <= 8):
    costo = float(11)
else:
    costo = float(10)

print(f"Costo por teclado : ${costo}")
print(f"Total a Pagar : ${costo * cantidad}")