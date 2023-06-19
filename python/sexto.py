#Pide dos numeros para determinar soi son pares o impares

numero1 = int(input("Digite un número: "))
numero2 = int(input("Digite otro número: "))

if numero1%2 ==0 and numero2%2==0:
    print("Ambos números son pares")
elif numero1%2 ==0 and numero2%2!=0:
    print("El primer numero es par y el segundo impar")
elif numero1%2 !=0 and numero2%2==0:
    print("El primero número es impar y el segundo es par")
elif numero1%2 !=0 and numero2%2 !=0:
    print("Ambos números son impares")
    
    