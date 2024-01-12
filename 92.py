

print("""
TIPOS DE SEGURO"
    1. X"
    2. Y"
    3. Z
"""
)

seguro = int(input("OPCIÓN"))

if (seguro == 1):
    print(f"Pago Mensual : $45")
elif (seguro == 2):
    print(f"Pago Mensual : $30")
elif (seguro == 3):
    print(f"Pago Mensual : $15")
else:
    print(f"Error en el tipo de seguro.")