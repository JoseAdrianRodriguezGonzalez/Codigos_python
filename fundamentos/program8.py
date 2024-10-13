# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 11:09:22 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripcion: List comprehension
"""
#Dada una lista con números flotantes,crear una nueva lista que contenga
#Los números de la lista originial, multiplicacods por 2
lista_1=[4,5,6,7,8,9]
lista_2_vieja=[]
for i in lista_1:
    lista_2_vieja.append(i*2)
print(lista_2_vieja)
lista_2=[x*2 for x in lista_1]
print(lista_2)
#item to append |loop over the iterable
#[item to append |for control in [iterable]]
#Nota when i need to create a new list, I can use list comprehension
#List comprehension always creates a new list

#Create a new list with even number in a given range
#Wth list comprehension using conditionales
lista_even=[ x for x in range(1,20) if not(x%2)] 
##Append in list only those items(i
#Produced by the itereable function that even
#Create a list with number that are even and divisible by in a rgien range
lista_even_five=[x for x in range(1,101) if not(x%2) and not(x%5)]
print(lista_even_five)
#Use of if .. ese
#create a list full of strings 'even' or 'odd'
lista_n=[ 'even' for x in range(1,20) if not(x%2)]
lista_n=[]
for i in range(1,21):
    if i%2==0:
        lista_n.append('Even')
    else:
        lista_n.append('Odd')
lista_n=[]
lista_n=['Even' if i%2==0 else 'Odd' for i in range(1,21)]
#Create a list full of strings 'even','odd','zero'
#if the numbes are even, odd, or zero
lista=[4,0,5,6,10,0,1,0,4,13,9,8]
lista_n=[]
for i in lista:
    if i==0:
        lista_n.append('Zero')
    elif i%2==0:
        lista_n.append('Even')
    else:
        lista_n.append('Odd')
lista_n_it=['Zero' if i==0  else 'Even' if i%2==0 else 'Odd' for i in lista]
print(lista_n_it)
###Nested lists
#Create a list of S lists, where eahc internal list
#Contains the sequence from 0 to 4
lista=[]
for i in range(5):
    temp=[]
    for j in range(5):
        temp.append(j)
    lista.append(temp)
    
lista=[[j for j in range(5)] for i in range(5)]
print(lista)
#Create a new list of lists with the of a list of lsits squared

lista=[[1,2,3],[7,8],[10,4,5],[11,12]]
lista_squared=[[j**2 for j in i] for i in lista]
print(lista_squared)

##Create a new lsit with the individual words of a 
#list of strings (sparated by space)
lista_s=['hola mundo','como estás','aquí todo bien']
new_lista=[]
for s in lista_s:
    words=s.split()
    for word in words:
        new_lista.append(word)
print(new_lista)
#                ciclco externo       ciclo interno
gene_list=[word for s in lista_s for word in s.split() ]
print(gene_list)

#Important 1. List comprehension is an elegant way to define lists based on existing items,(functions,items colections)
#2. list comprehension is generally more compact and FASTER tha normal functions and loops for creating lists. when creating
#new lists, list comprehensio si preferred.
#An d particularliy useful with very large lists.
#3. However, we should avoid very long lists comprehension in one line(on very complex ones), to ensuer the code is#
#User firendly and readeble.
#4Every list compreension can be reritten in a for loop, but not very for loop can be rewritten as a list comprehension 
