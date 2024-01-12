
d = 3
suma = 1

n = int(input("VALOR DE N"))

if (n > 1):
    print(f"{suma} + ", end = "")
    for i in range(2, n + 1):
        if (i == n):
            print(f"{i}/{d}", end = "")
        else:
            print(f"{i}/{d} + ", end = "")
        suma += (i/d)
        d = d + 2
        
print("La suma es :")
print(suma)