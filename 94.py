

bonificacion = 0


sueldo = int(input("Sueldo Base"))
categoria = int(input("Categoría : 1.A - 2.B - 3.C - 4.D"))

if (categoria == 1):
    bonificacion = sueldo * 0.1
elif (categoria == 2):
    bonificacion = sueldo * 0.2
elif (categoria == 3):
    bonificacion = sueldo * 0.3
elif (categoria == 4):
    bonificacion = sueldo * 0.5

print(f"BONIFICACIÓN : ${bonificacion}")
print(f"SUELDO NETO :  ${sueldo + bonificacion}")