num1 = int(input("Digite un número: "))
num2 = int(input("Digite otro número: "))
num3 = int(input("Digite otro número: "))

if num1==num2 and num1==num3:
    print("Todos son iguales")
elif num1>num2 and num1>num3:
    print(f"El numero {num1} es el más grande")
elif num2>num1 and num2>num3:
    print(F"El número {num2} es el más grande")
elif num3>num1 and num3>num1:
    print(F"El número {num3} es el más grande")
            