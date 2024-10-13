# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:39:08 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripición: Object identifier and types
"""

##En python aiwmpew tiene dos cosas
# Posee metodos y atributos
##Atributos: Caracteristica o propiedad del objeto
###Metodos: Accion o funcion que el objeto puede realizar
#En python

#Objeto lista:
    #Atributos: longitud
    #Metodos:append,extendremove,pop, insert,..
#object: str
#atributo longitud
#Método: lower upper, strp, split, etc..
#Los objetos en pytghon son absatracciones para los datos.
#Todos los datos en Python son representandos por objeto o por relaciones entre
#objetos
#Para sabersi tiene una identada en particular
a=5 #a es un objeto de case entero
print(id(a))
b=0.57#objeto float
print(id(b))
c=5
print(id(c))
##La identidad de un obejto es un entero del cual es generado a ser unico y
# constante
#oara cada uno de los objetos en su tiempo de vida
#Dos objetos con tiempos de de ejecucion distitnso, pueden obtener el msmo 
#numero

##Para python(cpython), id(x) se hace referencia a la direccion de memoria 
#donde se almacena x
#Python hace un cache para los valores de datos que son comunes,tales como
# strings, enteros, tuplas
#Asi que podemos encontrar multiples elementos que hacen referencia al mismo id
#si los valores con los mismos
c=6
print(id(c))
##Suponga que tengo el valor de 
a=[1,2,3]
print(id(a))
b=a #b esta referenciando a un objeto existente a
print(id(b))
b.append(6)
#Esto modifica el objeto referenciado y el objeto actual

#If i want to modify the ojbect b without modifying the reference
#object a, we need to copy the imtes form one list to another
b=[] #Createsa new object (list)
print(id(b))
b.extend(a) #copies all the items of a to b

print(id(a))
print(id(b))
b.append(7)
#Note: Be careful, thiw will only do a shallow copy
#copy of the basci types: int, float, str, imag
#If the internal object are mutalbe collections
#Sucha as lists. in that case these oculd still be modified
a=[[1,2,3],[4,5,6]]
b=[]
b.extend(a)
print(a[0][1])
a[0][1]=5000
#This will modify the internal tem in a and b 
#The id allow me to identify the object to be modified
print(id(a[0]))
print(id(b[0]))
for i in a:
    b.extend(i)
print(id(b))
print(id(a))
###Identitiy operator
x=['apple','banana','cherry']
y=x
print(id(y))
print(id(x))
print(y is x)
#Checks if two objects are the same Returns boolean
#Have the same id
a=[1,2,3] #Creates a new object
b=a #redirects
c=[1,2,3]
print(a is b)
#True a and b are same
print(a is c) 
#False, because c is a new object
print(a==c)
#True 
#Compara los objetos dentro de las colecciones en orden.
#a y c tienen los mismos objetos
#ay c son guales pero no son identicos
#no tienen el mismo id 

##Types of objects
a=12
print(type(a))
a=123.45
print(type(a))
a='Hola mundo!'
print(type(a))
if type(a)==list:
    print('a es una lista')
elif type(a)==int:
    print('a es un entero')
elif type(a)==float:
    print('a es un flotante')
elif type(a)==str:
    print('a es un string')
else:
    print('No recnozco el tipo de a')
    
#An object's type determines the operations that t objec supports()
#The 'does it have a length?'
#And also defines the possible values for objects of that type

# Every object in python has:name, type, value,identity
print('el nombre de la variabls es,a')
print(f'la identidad es {id(a)}')
print(f'el tipo de es a:{type(a)}')
print(f'El valor de a: {a}')
#he value of some objects can change
#The objects whose value can change are said
#To be mutable: objects whose value is 
#unchangabl once they are created
#are called immutable.
#An object's mutability is determine by its type.
#For example, strings and tuples are inmmutables
#While lists and dictionaries are mutable