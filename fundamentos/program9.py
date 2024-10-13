# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:51:16 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripición:Tuplas
"""
#una tupla en python es una colección ordenada de objetos,(por lo tanto es indexado)
#es decir, importa el orden de como se accede
#yo puede accceder a los objetos por su índice
#son como las listas, pero inmutables.
#no se pueden modificar
#Podemos colocar cualquier tipo de objeto dentro de una tupla
t=('tuples','are','like','lists','but','inmutable',4,[1,2])#tupla vacía
t2=('one-item tuple',)#siempre se colocan las comas cuando solo es un elemento
#is a tuple with one time(coma is necesarry)
t3=('one-item tuple')#si solo es un elemento, se considera string
print(t[0])#primer elemento
print(t[:3])#tuplas de los elementos desde cero hasta 3-1
#Si aplico el slicing en una lista -->devuelve una lista
#Si aplico el slicing en un string -->devuelve un string
#Si aplico el slicing en una tupla -->devuelve una tupla

#Las tuplas soninmutables
#t[0]='Assignment is not posible' #no se puede modificar
t4=t+('more elements',6,7,8)
#Creates a new tuple by concating two tuples 
t5=t+('only one item',)
#If it doesn't have the coma, will return an error due to the first one is a tuple,
#and the second one is a string
#The concatenation always creates a new tuple
t=t+(10,11,'hello',10)
#reeplaing the original value t with a new t
#Some useful methods
print(len(t))#length of the tuple
print(type(t))#return the tpye of the variable
print(t.index(10))
#Returns the index of he first occurence of 10
print(t.count(10))
#Return the number of times that 10 appears in t
###Repetition
t6=t*2
#creates a new tuple with t repeated 2 times 
print(t6)
##lists to tuples to lists
a=[(1,2),(3,4),(5,6)]#A list of tuples
b=([1,2],[3,4],[5,6])# a tuple of lists
c=tuple(a) #it can a cast to tuple
d=list(b)#you put a tuple and it casts to a list

##In and not in operators
if('tuples' in t):
    print('Yes!!!!!!!!!!!')
else:
    print('Noooo!')
    
if (4 not in t):
    print('Yes!')
else:
    print('no')
#Iteration over tuples
for i in t:#t is iterable
    print(i)
#Negative indexing
print(t[-4::-1])
print(t[::-1])#nverse
for i in t[::-1]:
    print(i)#inverse iteration
#unpacking tuple
t7=('a','b')
x,y=t7
r={
   'r':'a',}
#tuples unpacking, eachobject in the left takes an item 
#from the tuple in the right
#we need to put as many obejcts in the left as items in the tuple
#Tuples are faster than lists, tjeu are usfuel when a collection
#of objects is not going to change during the program execution
#the collection is static
#We can't add items to a tuple once it is create.
#Cannot be append or extended 
#we cannot remove items from a tuple once it is created.
# if you need to add, remove, or modify objects in a tuple frequently, use instead a list
#If we need create a tuple form scratch(starting from an empty collection) first create
# a list (prefearebe using list comprehension) and afterwards transform it into a tuple