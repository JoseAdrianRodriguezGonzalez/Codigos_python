# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 10:18:16 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción:Basic use of functions
"""
#Para generar una función se usa la sintacis:
    #def [nombre de la funcion](param1,param2,...):
        #Los dos puntos indican el termino de la funcion
        #S partir de ahí siguen las instruccione propias de la función
        #Hay dos elementos basicos. El parametro y el argumento
        #param: es el nombre del objeto que se le pasa a la función
        #def greet(nombre)->nombre del parametro
        #argumento-> es el valor del objeto cuando se llama a la función
        #greet('Pedro'), pedro es el argumento que se pasa a la función
        #la función
def greet(name):
    """
    Imprime un saudo de buenos días para una persona

    Parameters
    ----------
    name : str
        Nombre de una persona.

    Returns
    -------
    None.

    """
    print(f'Hello {name}. Good morning!')
    return #return devuelve el flujo de control al puno de llamada de función
#Si no se pone puede funcionar, pero puede llegar a marcar errr. Es recomendable ponerlo
#Indica que en esa parte irán algunes instruccion, pero todavía nos ep cuales
#Se usa para evitar el error de sintai en la defincion
# de estructuras de control: ifs, fors, whiiles, defs..
#Toda funcion tiene un scope local.
#Es decir, las variables que s rean dentro de la funcion
# solo exiten dentro de ella.
#No puede llamar  a esas vairales desde fuera de la funciónn.
#Todo parámetro que se pase a una función, se pasa por referencia
# sepasan por la direcció de memoria (id)
# Si modifico el parametro de la funcion, si es mutable. También se modifica el objeto que s epaso como argunmento
greet('Perla')
greet('Pedro')
#Returning a vlaue

def absolute(num):
    """
    Calcula y deuele el valro abosuluto de un número

    Parameters
    ----------
    num : Float
        un numero para calclar el valor absoluto

    Returns
    -------
    None.

    """
    if num<0:
        num*=-1
    return num
n=absolute(-5)
print(n)
def greet_two(name):
    """
    
    Imprime un saludo de buenos dias para una persona y devuelve la version en mayusculas, y la version en minuscuals de l nombre de la persona.
    
    Parameters
    ----------
    name : str
        DESCRIPTION.
        Es el nomrbe de una persona
    Returns
    -------
    up : str
        DESCRIPTION.
        la versión en mayúsculas de nae
    lw : str
        DESCRIPTION.
        La versión en minuscula de name
    """
    print(f'Hello{name}.good morning')
    up=name.upper()
    lw=name.lower()
    return up,lw
#Cuando se devuelven mas do o más valores, los valroes, se devuelven como una tupla.
#Loq ue en realidad de veuvle es un objeto como un tupla
up,lw=greet_two("Perla")#Se desacomplan los valores de la tupla que son devueltos por la función
def greet_three(name,msg='Good morning'):
    print(f'Hello {name}, {msg}')
    return
    """
    
Imprime un mensaje de saludo para una persna
    Parameters
    ----------
    name : str
        DESCRIPTION.
    msg : str
        DESCRIPTION.

    Returns
    -------
    None.

    """
greet_three('María','How do you do?')
greet_three('Perla')
def greet_four(*names):
    """
    
    Imprimie un saludo para cada una de las personas que s epasan coo argumentos.
    Parameters
    ----------
    *name : TYPE
    Una secuencia de nombres de personas.

    Returns
    -------
    None.

    """
    print(names)
    for name in names:
        print(f'hello{name}: good morning')
    #Recibir una cantidad no definida de argumentos
    #Los argumentos s eguardan en names, como una tupla
    return
greet_four('luis','pedro','susana',5.6)
### try, except
try:
    greet('Ana','Uwu')
except:
    print("Hya un error en la llamada a la función")
print("Esto tambine se ejecuta")