


numero = int(input(f"Ingresa Un Numero PRIMO:  "))
isPrime = "ES PRIMO"

for i in range(2,numero):
    if (numero%i) == 0:
      isPrime = "NO ES PRIMO"
    

print(isPrime)