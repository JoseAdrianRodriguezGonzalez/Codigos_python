#Calculadora aritmetica
print("S,s = Suma\nR,r = Resta\nM,m = multiplicación\nD,d = división ")
operacion = input("¿Qué operación quiere hacer? ")

if operacion == 'S' or operacion == 's':
    print("Suma\n")
    num1= int(input("Digite el primer valor: "))
    num2= int(input("Digite el primer valor: "))
    resultado = num1 + num2 
    print(f"El resultado es: {resultado}")

if operacion == 'R' or operacion == 'r':
    print("Resta\n")
    num1= int(input("Digite el primer valor: "))
    num2= int(input("Digite el primer valor: "))
    resultado = num1 - num2 
    print(f"El resultado es: {resultado}")
    
if operacion == 'M' or operacion == 'm':
    print("Multiplicación\n")
    num1= int(input("Digite el primer valor: "))
    num2= int(input("Digite el primer valor: "))
    resultado = num1 * num2 
    print(f"El resultado es: {resultado}")
    
if operacion == 'D' or operacion == 'd':
    print("División\n")
    num1= int(input("Digite el primer valor: "))
    num2= int(input("Digite el primer valor: "))
    resultado = num1 / num2 
    print(f"El resultado es: {resultado}")
else:
    print(f"No está ese valor")