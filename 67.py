

altura = 0

while ((altura % 2) != 1):
    altura = int(input("Altura del rombo"))

for i in range(1, altura + 1, 2):
    for j in range(1, int((altura - i)/2 + 1)):
        print(f" ", end = "")
    for j in range(1, i + 1):
        print(f"*", end = "")
    print("")

for i in reversed(range(1, altura - 1, 2)):
    for j in range(1, int((altura - i)/2 + 1)):
        print(f" ", end = "")
    for j in range(1, i + 1):
        print(f"*", end = "")
    print("")