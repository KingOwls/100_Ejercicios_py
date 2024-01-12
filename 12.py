

numeroUno = int(input("Numero A"))
numeroDos = int(input("Numero B"))

numberMayor = 0

if(numeroUno < numeroDos):
    for i in range(numeroUno, numeroDos):
        print(i)
else:
    for i in range(numeroDos, numeroUno):
       print(i)
