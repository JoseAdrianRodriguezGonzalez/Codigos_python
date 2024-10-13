# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:44:51 2024

Descripción: Lists II
"""

##Useful methods /functions
b=[1,2.2,'python',[4,5,6]]

b.insert(2,3) #Inserta en la posicion 2 el 3
last=b.pop() #Extrae el elemento de la ultima posicion
second=b.pop(1) #Extrae el elemento en la posicion 1
b.insert(0,'a')
b.append('a')

b.remove('a')#remuece la primera ocurrernica de 'a

b.insert(2,'c')
b.append('c')
b.index('c') #imprimir el primer indice de la ocurrencia 'c'
a=[1,2,3,4,5,6,7]
c=a+b #Permite concatener dos lsitas

##Repeticion
d=b*3 #lista b se repite 3 veces en la nueva lista d

a.extend(b) #Le añade todos los elementos con la lista b
#extende modifica la lista original
#mientras que la concatenación necesita crear una nueva lista 
#Si necesito añadir items a la lista existene, usamos extend
#if necesitamos crear una lista desde la concatenacion de dos o mas listas,
# usamos el operador

##La concattenacion es menor eficiente por el hecho de crear nuevas listas
##extend es eficiente debido a que nos basamos de una lista ya existente.

###OPeradores de memebresía
#Devuelven valores true o false
print('a' in b)## true
print('z' in b)##false

##complemento
print('a' not in b) ##comprueba si no esta false
print('z' not in b)##true

##otros metodos

print(c.count('c')) # cuenta el numero de veces que algo aparece en la colección
g=[12,20,15,8,1,3,250]
g.sort()#Ordena los itemas en orden ascendente (in place)

g.sort(reverse=1)#ordena en descendiente
##Para aplicar los metodos sort, tood slos items dentro de la lista deben ser 
#del mismo tipo
h=['hola','que','tal','como','estas']
h.sort()
#b.sort() ##No es soportado porque contiene items de diferente tipo
t=['Hola','que','tal','ala','Alejandra','Bonito']
t.sort()## orden lexicografico (por posicion del caracter en la tabla de codificación)
###