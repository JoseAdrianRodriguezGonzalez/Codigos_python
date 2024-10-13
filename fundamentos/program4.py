# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:12:37 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción: Listas I
    
"""
# Las listgas son colecciones de cosas
#Las listas son colecciones ordenadas (ordered) de objetos 
#-->El orden de inserción Si importa. EL orden e mantiene a lo largo de la
#ejecuión
#--> Los objetos están indexados {Cada objeto en la colección}
#Tiene n indice
#Podemos accedre a los objetos por su indica(por posición)
#Los objetos en una lista no tieen que ser del mismo tipo.
#Las listas son mutables --> Podemos cambiar los objetos
#que están ubciados en un indica especifico
#Las list son como los arreglso pero más felxibles
#Las sintáxis básica es nombre_lista=[obj_1,obj_2,...]
a=[1,2,3,4,5,6,7,8,9,10]
b=[1,2.2,'python',[4,5,6]]
c=[]#mpty list

#access by index
#Positive index(from o then len(list)-1)
#From left to right
print(a[0])
print(a[2])



##Accesing several items at the same time
#slicing returns a list that is  sub-list of the bigger one
print(a[2:6:2])#slicing :return the items from index to 6-1
#format slicing [val_ini:val_fin:step] the value of step is 1 by default
#the val_ini is 0 and val_fin len(a)-1 if it is not written
print(a[0:9:2])# return the values of 0 to 9 with a step of 2
#Negative index from 0-1 to 0-len(list)
print(a[:-5]) #returns form 0 to -5+1
print(a[-5:]) #return from -5 to the end
print(a[-5::2])
print(a[::-1]) #Returns all the itmes from list in reversed order
print(b[-1]) #return the last item of b
print(b[-1][0]) #return the last item of b and the first value
#mutate the list
b[1]="js"
b[-1]=["Hola","mundo",6,7,8]
#Add items to lists
b.append("Hundres") #Add an item at the end of a list
c.append("hello")
c.append([1,2,3,[3,4,5]])
b.extend(['a','b','c',34.5])
         
 # Extends a list with another list
 #Extens b with the list passeda parameter
 #EACH ITEM OF THE NEW LIST IS APPENDED INDIVIDUALLY)
 #At the end of th original list
 
r=[]
r.extend([a,b,c])


print(len(r),len(a),len(b))

### list iterations
# Accsing by item
#a list is an iterable object
i=0
for i in b:
    print(i) #items from b are accesed in order
for i in b[5:]: #i iterates over a slice of (from index 5 to the end)
    print(i) 
for i in b[5:7]: #i iterates over a slice of (from index 5 to 6)
    print(i) 
for i in b[::-1]:
    print(i)
    
## Accesing by index
for i in range(len(b)): #Iterates over the indexes of b
    print(i,b[i]) #i is the index, b[i] is the item at index 
    
###List of list
lista=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print(lista[1][1])
for i in lista:
    print(i)
for i in lista:
    for j in i:
        print(j)