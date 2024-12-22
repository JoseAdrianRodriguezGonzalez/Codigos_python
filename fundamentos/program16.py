# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:29:24 2024


@author: USUARIO
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Lambda functions
"""
#Ua función Lmabda es una función pequeña y anonima,(no tiene nombre)
#Esta sujeta a una sintáxis más restrictiva pero más compacta, que una función regular en python.
#Una función Lmabda puede tomar cualquier numero de argumentos pero solo puede tener una expresión.

#En otros lenguajes se les conocen como:
    #Funciones anonimas o literales
    #En javascript son arrow functions

def identity(x):
    return x
print(identity(5))
#with a lambda function
lambda x : x**x
#Sintaxis es lambda tiene el argumento y luego la expresion
#La expresion pueden ser otras funciones que me regresa otro valor, 
#El uso de la funcion lambda se llaman así
(lambda x : x**x)(2)

def add_one(x):
    return x+1
print(add_one(5))
add_one=lambda x:x+1
add_one(4)

#Una función lambda recibe varios argumentos
def add_two(x,y):
    return x+y
(lambda x,y:x+y)(1,2)
add_two=lambda x,y:x+y
add_two(2,5)
full_name=lambda first, last: f'Full name: {first.title()} {last.title()}' #Los transforma a formato de titulo
print(full_name('jose', 'adrian'))

suma=lambda a,b,c:a+b+c
print(suma(1,2,3))
que=lambda x: x if (x>=10) else 10
que(15)
#Notas:
#Si es necesario construri una expresion demasiado compeaja tal vez sea mejor
#utilizar una función normal
#Los statemnets no pueden ser utilizados en las funciones
#lambda, a eces pude ser mejor utilizar una funcion normalmente defindia

#Las funciones lambdas deberian ser anonimas
(lambda x:x)(5)
(lambda x:x if(x>10) else 10)(15)
####High order functions
#lambda functions
#son frecuentemene usadas en funciones de orden superior
#van a tomar una o más fucnitones comoa rgumentos y o van a regresar
#una o más funciones
def plus(x,b):#x ,bpueden ser funcione slambda
    c=lambda x:x
    return c #c puede ser lambda function
plus(lambda x:x+1,lambda x: x*2)
high_ord_func= lambda x, func : x+func(x)
high_ord_func(2, lambda x:x+5)
##Use with some built in function
##that take a functionas as an argument
###filter()
#Select certain items from an iterable based on predifined
#criteria#Syntax:
#filter(function, iterable)
lista=[33,3,22,2,11,1]
#Filter values >10
#1. With list comprehension
lista_2=[x for x in lista if x>10]
#2. filtro
lista_3=filter(lambda x: x>10,lista)
for i in filter(lambda x: x>10,lista):
    print(i)
tupla=tuple(filter(lambda c:c>10,lista))
#Las funciones iterables generan un solo valor en cada iteracion+
#del ciclo
#eso ahorra memoria, porque no se genera toda la seucncai de una sola ve
#ahorra tiempo, en caso de que no esea necesario recorrer todos
#los eleemntos de la seucnecia
## Aplica una cierta operacion para cada objeto del iterable 
#synatx:
    #map(func,iter)
    #
lista_4=[x*10 for x in lista]   
lista_5=list(map(lambda x: x*10,lista))

##Key functions
#Key functions are high order functions that take a parameters
#a key as a name argument
#key receives a fucntion tha can ba a lambda
#This function directly influences the algorithm driven by the key function itself
#the key parameter key returns a vlaue taht is used by the high order funcition
#SOme key fucntions sort,minmmax,sorted
ids=['id1','id2','id30','id3','id4','id22','id100']
print(sorted(ids))
#returns a sorted list of th itmes
#Está ordenando los elementos de forma lexicografica es decir
#por la posicion del caracter en la talba de codificacion
#1. compara rel primer caracter

#Queremos ordernalo por el valor numerico despues de los caracteres id
sorted_ids=sorted(ids,key=lambda x: int(x[2:]))
#x toma cada elemento del iteralv id
#la funcion key regresa el valor entero de la subcadena x[2:]
#El valor devuelto por la funcion key es el criterio
#utilizando por sorted para ordenar
print(sorted_ids)





menu_items={
    'Fries':1.00,
    'Apple':0.25,
    'Orange':0.68,
    'Mac n cheese':0.75,
    'Pizza slice':0.80,
    'Fresh oven-baekd biscuits':0.35
    }
#Diccionario
#name:price
#asi directo la funcion max se aplcia sobre los keys del diccionario
#Las llaves son cadnes, por lo que s eocmparan lexicograficamente
#Por posicion en la talba de codificación
#-->la letra en la posicion más alta en la talbe es P
max_item=max(menu_items,key=lambda x:menu_items[x]) #X es la key del diccionario
#El parametro x en la funcion es cada llave del diccionario
#menu_ims[x] devuvel el valor asociado con cada llave x
#El valor que devuel la función lambda se utiliza en la funcion max para jacer ñas cmparaciones.
#key with the maximum price
print(max_item,menu_items[max_item])
max_word=max(menu_items,key=lambda x:len(x))
#El paametro x en la funcion lambda es cada llave del diccionari
#la funcion lambda se develve la lonfitud de cada lllave x
#key with maximum length
tuplas=[(3,7),(2,12),(5,10),(9,0)]
tuplas.sort()
#Cambiar el criterio de ordenamiento
tuplas.sort(key=lambda x:x[1])
#El parametro xe n la funcion lmbda es cada tupla interna de la lista
#el valor regresado por la funcion lambda e sutilizado por la funcion sort como cirterio para ordenar
#