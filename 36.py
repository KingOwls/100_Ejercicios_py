



sumatoria = 0
v = 4
v1 = 5
v2 = 1
x = 2
x1 = 0.5
ope = "-"

numero = int(input("Ingresa un Numero"))

for i in range(1, numero + 1):
    if (i != numero):
        print(f"{v}/{x} {ope} ")
    else:
        print(f"{v}/{x} {ope} ...")
        
    if ((i % 2) == 1):
        ope = "+"
        sumatoria = sumatoria + (v / x)
    else:
        ope = "-"
        sumatoria = sumatoria - (v / x)
    v = v + v1
    v1 = v1 + v2
    v2 = v2 + 1
    x = x * x1
    x1 = (x1 + x1)


print(f"SUMATORIA : {sumatoria}")