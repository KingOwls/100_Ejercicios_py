

var = 1
a = 1
b = 5

showLista = []

for x in range(1,10):
    showLista.append(a)
    showLista.append((x * 5))
    print(f"{a}")
    print(f"{x * 5}")
    a += 6

print(showLista)