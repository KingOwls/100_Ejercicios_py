pares = 0
impares = 0


Cant = int(input("Ingrese la cantidad de numeros a ingresar:  "))
for i in range(Cant):
    numero = int(input(f"Ingresa Un Numero"))
    if ((numero % 2) == 0 ):
        pares += 1
    else:
        impares += 1

print(f"Numeros Pares {pares}")
print(f"Numeros Impares {impares}")