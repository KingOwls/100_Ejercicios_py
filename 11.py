
numero = int(input("Valor de N"))

prod = 1

for x in range(1, (numero + 1)):
    print(prod)
    prod = (prod * x)
print(f"El producto de {numero} es = {prod}")