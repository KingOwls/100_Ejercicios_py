

lista = []

for x in range(9):
    x += 1
    for i in range(10-x):
        lista.append(10-x)

    print(lista)
    lista = []