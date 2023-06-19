edad= int(input("Digite su edad "))

if 0<edad<100 :
    print("Edad correcta")
    if edad>=18:
        print("Mayor de edad")
    else:
        print("Eres menor de edad")
else:
    print("No existe")
