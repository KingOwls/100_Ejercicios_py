
numero = 0


while (numero <= 100) and (numero <= 999):
    numero = int(input("Ingresa un Numero de Tres Cifras"))

numero = str(numero)
print(f"CENTENA: {numero[0]}")
print(f"DECENA: {numero[1]}")
print(f"UNIDAD: {numero[2]}")