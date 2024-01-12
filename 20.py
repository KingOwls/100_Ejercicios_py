
import random
vidas= True
randomNumber = random.randint(1, 10)
print(randomNumber)
print("Se genero un Numero Aleatorio entre 1-10")

while(vidas):
    numero = int(input("Ingresa un Numero del 1-10"))
    if (numero < randomNumber):
        print("El Numero es Mayor")
    elif(numero>randomNumber):
        print("El Numero es Menor")
    if (randomNumber == numero):
            print("Numero correcto")
            vidas=False

print("FELICIDADES GANASTE EL NUMERO ADIVINAR ES CORRECTO")
