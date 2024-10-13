# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 10:16:15 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripición:Sets
"""

#Sets on python are unordered collections of items
#Insertion order is not manteined. We can access to the elements by their position.
#Other property: the elements from the sets are uniques, so there won't be duplicated.
a=set()#Empty set

a={1,2,3,4,5.5,'sets','uwu','b','c'}# the set definition use {}
a={5,1,2,3,3,4,5,5,3,2,1} #A set is a collection of unique items the repeated items are erase it
#A set by itselft is mutable,but the elements inside of it must be of an immutable type
temp={1,2,3,(3,4)}#sets can not contain mtable objects
temp={1,2,3,(3,4)}
#Sets are unordered (insertion order does not matter)

print(len(a))#Returns the length of the set
print(type(a))# returns the type of data,(set)
b={3,4,5,6,7,8}
print(a.union(b)) #Returns the union of values joined between both sets.
print(a.intersection(b))#returns the intersection of A an B
print(a.difference(b))#Returns the elemnts that are from A both they aren't on B
print(b.difference(a))#Returns the elements from b that are not in a
print(a.symmetric_difference(b))#returns the set that are  in A and B, but they are not between them
print(a.isdisjoint(b))#returns true if a and b have no items between both sets
c={1,2}
print(c.issubset(a))#Retruns a boolean value if c is  subjoint of A
#that it means if the sets is contained on A.
print(a.issuperset(c)) #Returns if A is superset of c
##in and not in are available for sets
if 'sets' in a:
    print('Yes!')
else:
    print('no!')
if 4 not in a:
    print('Yes!')
else:
    print('no!')
#Sets are mutable
a.add('hola')##Add an element to the set a
a.update(['one','two','three']) #Updates a with items from a list
a.update(('four','five'))#And with tuples are equal
a.update({'six','seven'})#Also, it can add elements from a set
a.add(('hola',1,2,3))#ere it add a tuple to a, so it ispossible, because is inmutable
#but if you try to add a list on a, it will not be possible due to lists are mutable}
#You can remove elements
a.remove(3)#remove an element from a(Items from a set are unique)
print(a.pop())#Extracts the last element from a set, however, the sets are not ordered, we 
#we will not know which objet will be trashed.
#Iteratpn over a set
for i in a:
    print(i)
    #Itereates over each item of set a
    #but there is no guarantee about the order in with the items will be accessed
#If we need to acces the items insta a set ina specigic
#order we need to use on ordered collection(lists,tuples)
#Lists,tuples to set to list,tuple
e=[1,2,3,'hola',3,4,5]
f=(1,2,3,'hola',3,4,5)
g=set(e) #list to set
h=set(f) #tuple to st
l=list(a)#A set to list
t=tuple(b)# A set to tuple
#We don't know the order the items will be allocated.
#Sets musn't be used to acces items in a specific order
### Set comprehension.
# it is possible to apply a comprehension, becaucse sets are mutable
#create a set of unique even numberse between 1 and 20
s={x for x in range(21) if not(x%2)}
s=set()
for i in range(21):
    if i%2==0:
        s.add(i)
#Notes are much faster than lists and tuples
#They are useful when a collection contains unique items