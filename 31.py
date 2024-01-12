refran = input("Ingresa un Refran :>").upper()

C=0
S=0
D=0
L=0
R=0
M=0

consonante = 0

for i in refran:
    if (i == "C"):
        C += 1
    elif(i == "S"):
        S += 1
    elif(i == "D"):
        D += 1
    elif(i == "L"):
        L += 1
    elif(i == "R"):
        R += 1
    elif(i == "M"):
        M += 1
    elif((i == "A") or (i == "E") or (i == "I") or (i == "O") or (i == "U")):
        consonante += 1


print(f"CANTIDAD DE C {C}")
print(f"CANTIDAD DE S {S}")
print(f"CANTIDAD DE D {D}")
print(f"CANTIDAD DE L {L}")
print(f"CANTIDAD DE R {R}")
print(f"CANTIDAD DE M {M}")

print(f"CANTIDAD DE CONSONANTES {consonante}")