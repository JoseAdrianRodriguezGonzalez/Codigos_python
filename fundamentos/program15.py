# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 11:18:42 2024

@author: USUARIO
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Built-in function
"""
#Fucniones que no requieren un modlo o pauete para trabajar
#No necesitmaos importarles nada
#Estas funciones ya está directamente construidas en el kernel de python
#Built- in functions are highlighted in differnt color
print(range(5))#funcion iterable
print(type('hola'))#Devuelve el tipo del objeto
print(str(5.6))#Castea un valor a str
print(int('5'))#Convierte un objeto a int
print(list((3,4,5)))#convierte la tupla a lista
print(tuple())#Convierte la lista en tupla
print(set())#Convierte la lista en un conjunto
print(dict())##Convierte una serie de parametros

## some other useful functions
print(abs(-16))#valor absoluto
print(round(15.4121232,2))#devuelve un valor flotante que es una version redondeada con un numero especifico de decimales
print(chr(10014))#Devuelve el caracter unicode en la positicion 97, dentro de la tabla de codificacion
print(ord('ñ'))#Cual es el entero para un caracter unciode ñ 241
print(ord("á"))#Saber cual es el valor de codigo unciode
print(divmod(10,3)) #devuelve una tupla con el cociente y residuo de a division
#Enumerar objetos d euna colleccion
seasons=['spring','summer','autumn','winter']
for season in seasons:
    print(season)
for i,season in enumerate(seasons): #i takes the count of each itme seasons inside the iterable seasons
    print(i,season)
#enumerate es una funcion iteralbe igual que range que para cada iteracion retorna un tupla con la cuent ay e valor para cada objeto
#del objeto iterble
#Genera una tupla cada vez para cada iteracion
for i,season in enumerate(seasons,10):#i va a tomar la cuenta de cada item seasons dentro del iterable seasons, pero va a empezar en un valor 
    print(i,season) #determinado
a=[1,6070,34,14,183]
b=['a','b','c','d','e','zapato','h']
c=[1.4,2.5,3.6]
d=[1.5,6,7,2.4,'a','b']
print(sum(a))#suma los objetos de un iteralbe
#suma para objetos numericos
print(max(a))#ddevuelve el objeto más grande dentro de una coleccion, con la restriccion de que los objetos de la colecicon
#deben ser dle mismo tipo
print(max(b))
#Sis e quiere hacer con d, no se puede ya que son del mismo tipo
print(min(a))#devuelve el objeto mas pequeño de una coleccion y los items de la coleccion de la colecciond deben ser del mismo  tipo
print(min(b))
#Inviertendo el ordeno de los objetos en una coleccion
a1=a[::-1]#genera una lista que tieen el orden invertido de la lista original
reversed(a)#devuelve los objetos dentro dle iterbale n orden inveros
for i in reversed(a):
    print(i)#imprimer los elementos de a en orden invertido
    #Reversed devuelve cada obejto de cada iteracion
a1=list(reversed(a))#genera una lista que tiene el orden invertido
#Ordenando objetos en una coleccion
a1.sort() #ordena la lista in place, la lsita se modifica
e=sorted(a)#devuelve una nueva lista ordenada a partit de un iterable, esto no modifica el objeto que se pasa
f={9,14,1,2,3,10}
g=sorted(f) #genera una nueva lista ordenada apartir de conjuntooo
t=(9,14,1,2,3,10)
h=sorted(t) #genera una nueva lista ordenada apartir de la tupla





##Acoplando elementos de varias listas(colecciones) al mismo tiempo
for i in range(len(b)):
    print(a[i],b[i])
##Las lsitas son de diferente tamñao para evitar el error de fuerea de rango
#necesito saber primero cual es la lista más pequeña

zip(a,b)#Funcion iteralmeb que para cada iteración va 
#generar una tupla con la combinación de elementos
# de diferentes iterables.
#Similar a otras funciones iterables, generalmente ttrabajan
#dentro de ciclos (for)
for i,j in zip(b,a):
    print(i,j)
for t in zip(a,b):
    print(t)
for t in zip(a,b,c):
    print(t)

for t in zip(a,f):#una lista y un conjunto
    print(t)
    #i,j toma los eleementos de la tupla gneradao de la iteracion de zip
    #zip se detiene een le iterable más pequeño
    #zip permite create n tuplas para n iterables
for t_1 in zip(a,t):#una lista y una tupla
    print(t_1)
    
    
#zip puede generar una lista de tuplas con la combinacion de 
#objetos de varios iterables
lista=list(zip(a,b,t))

#Todos los objetos que creo, se quedan en el scope principal
#Puede llegar un momento en donde la memoria se satura, debido a la cantidad o tamaño de los objetos.

#Python utiliza un recolector de basura(garbage collector)
#para liberar meomria, caundo los objetos ya no sn putiles
#Esti lo ahce de manera automática. No pdoemos
#controlas ese proceso.
#Una alternativa es eliminar los objetos desde código
#Sin embargo, esto no libera de inmediato la memoria, esta
#se libera hasta que ele garbarg collector entra en acción .
del a,b #Elimina los objetos del scope
#Esto ayuda para decirle al gabarg collector que so ya no
#se usara