

altura = float(input("Altura del Triángulo"))
caracter = float(input("Ingrese un Caracter"))

for i in range(1, altura + 1):
    for j in range(1, (altura - i) + 1):
        print(f" ", end = "")
    for j in range(1, (i * 2)):
        print(caracter, end = "")
    print(f"")