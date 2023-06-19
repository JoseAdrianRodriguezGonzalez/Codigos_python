nip= int(input("Ingrese su nip: "))
contador =0
di=1000
if nip == 1234:
    print("Ingreso exitoso\n")
    print("\t\tMenu\n\t1.Ingresar dinero\n\t2.Retirar dinero\n\t3.Saldo\n\t4.Salir")
    valor = int(input("¿Cuál menú quiere abrir?"))
    if valor==1:
        ing=float(input("¿Cuánto dinero quieres ingresar? "))
        di+=ing
        print(f"Quedan: {di} pesos")
    if valor==2:
        re=float(input("¿Cuánto dinero quieres sacar? "))
        di-=re
        print(f"Quedan: {di} pesos")
    if valor ==3:
        print(f"Hay {di}")
    if valor ==4:
        print("Adios")
        
else:
    print("Nip incorrecto")
    ++contador 
    if contador ==3:
        print("Se bloquea la cuenta")    