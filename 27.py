
divisible = 0
numero = int(input("Ingresa un Numero"))

for cont in range(2, numero + 1):
    for divi in range(1, cont + 1):
        if ((cont % divi) == 0):
            divisible = divisible + 1
    if (divisible == 2):
        print(cont)
    divisible = 0
    
