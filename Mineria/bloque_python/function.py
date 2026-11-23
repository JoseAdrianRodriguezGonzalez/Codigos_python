#Sintaxis
#def nombre_funcion(párametros):
#   return

def funcion_1():
    print("Hola mundo")
    return
def funcion_2(nombre):
    print(f'Hola {nombre}')
    return
def funcion_3(nombre="persona"):
    print(f"{nombre}")
    return 
funcion_1()
funcion_2("hola")
funcion_3()

#Cuadrdo de un número 

def cuadrado_(n=0):
    return n**2
def cuadrado(n=0):
    return n**2,n**0.5,n**3
def suma(lista=[]):
    try:
        sum(lista)
        return sum(lista)
    except:
        print("Error al realizar")
s=cuadrado_(2)
print(s)
#Rellena con un cierto caracter  "s:03"
print(suma([1,2,3,4,5,6,7,'l']))

cuad,raiz,cubo=cuadrado(2)
print(cuad,raiz,cubo)

#cuadrado,_,cubo=cuadrado(4)
#print(cuadrado,cubo)

print(cuadrado(4)[0])
