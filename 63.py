
costo = int(input("Costo de la Casa"))
iva = int(input("Valor del IVA"))

TotPagar = costo + (costo * (iva / 100))

print(f"IVA DE {iva}% : ${(costo * (iva / 100))}")
print(f"TOTAL A PAGAR : ${TotPagar}")