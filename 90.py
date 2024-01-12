

num1 = int(input("NÚMERO 1"))
num2 = int(input("NÚMERO 2"))

print("""
    [1 +]
    [2 -]
    [3 x]
    [4 /]
"""
)
operador = int(input("OPERADOR"))

if (operador == 1):
    print(f"SUMA : {(num1 + num2)}")
elif (operador == 2):
    print(f"RESTA : {(num1 - num2)}")
elif (operador == 3):
    print(f"MULTIPLICACIÓN : {(num1 * num2)}")
elif (operador == 4):
    print(f"DIVISIÓN : {(num1 / num2)}")
else:
    print(f"OPERADOR INCORRECTO")