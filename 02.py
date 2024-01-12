


pares = []
impares = []

for x in range(12):
        numero = int(input(f"Numero {(x + 1)}"))
        if (numero % 2) == 0:
            pares.append(numero)
        else:
            impares.append(numero)
print("CANTIDAD DE PARES = ")
print({len(pares)})
print("CANTIDAD DE IMPARES = ")
print({len(impares)})