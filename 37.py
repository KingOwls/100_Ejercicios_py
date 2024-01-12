M = []

numero = int(input("INGRESE DIMENSIÓN [MENOS O IGUAL A 20]"))

for IZQ in range(numero):
    M.append([])
    M[IZQ].append(1)
    for DER in range(1, IZQ):
        M[IZQ].append(M[IZQ - 1][DER - 1] + M[IZQ - 1][DER])
    if (numero != 0):
        M[IZQ].append(1)

for IZQ in range(numero):
    print(* (numero - IZQ))
    for DER in range(0, IZQ + 1):
        print("{0:2}".format(M[IZQ][DER]))
    print()