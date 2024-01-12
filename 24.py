fact = 1
numero = int(input("Ingresa el numero a calcular"))

print("SERIE DEL FACTORIAL : ")

Distancia = numero + 1
for x in range(1,Distancia):
    print((numero + 1) - x)
    fact = fact * x

print("EL FACTORIAL ES : ")
print(fact)
