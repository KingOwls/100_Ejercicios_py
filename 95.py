

N1 = int(input("Ingrese Nota 1"))
N2 = int(input("Ingrese Nota 2"))
N3 = int(input("Ingrese Nota 3"))

prom = round((N1 + N2 + N3)/3)

if (prom >= 0 and prom <= 10):
    print(f"NIVEL MALO")
elif (prom >= 11 and prom <= 13):
    print(f"NIVEL REGULAR")
elif (prom >= 14 and prom <= 16):
    print(f"NIVEL BUENO")
elif (prom >= 17 and prom <= 20):
    print(f"NIVEL MUY BUENO")