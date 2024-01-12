

boni = 0
sueldoF = 0

nom = input("Ingrese Nombre")
sueldoB = int(input("Sueldo Básico"))
hijos = int(input("Numeroo de Hijos"))

if (hijos > 0):
    boni = sueldoB * 0.7

sueldoF = sueldoB + boni

print(f"BONIFICACIÓN : S/.{boni}")
print(f"SUELDO FINAL : S/.{sueldoF}")
