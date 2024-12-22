# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 10:15:51 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripición:Diccionarios.
"""
#A dictionary is a mutable and ordered collection.
#of pairs 
#key:value
#Ordered means insertion order matters.
#Dictionaries are optimized to retrieve information.
#Key must be of inmutable type
#(not a list, set or dictionary)
#keys are unique, there could not be two keys with
#the same value.
#Values could be of any type
d={}#empty dictionary
d={'uno':'value_1','number':2,3:'test',(1,2):4.56,'hola':[1,2]}
#the key must be inmmutable however the value can be any type of data
# Notes :
    #A dictionary is similar to a JSON format.
    #A dictionary is similar to a LinkedHashMap
    #A dictionary is similar to a list(or an array),but
    #instead of an index to access an item (value), we use a key
print(d['uno'])# Returns the value associated
#with key 'uno'
print(d['number'])# Returns the value asssociated with key 'number'
print(d[3]) #Returns the value associated with key 3
# 3 is not an index is a key 
print(d[(1,2)])
#You can not acces as a key print(d[2])
print(d.get(3))
print(d.get('number')) #return the value associated with key 'numbers'
print(d.get(2)) #Returns None when the key does not exist
d['uno']=1378 #Change the value associated with key 'uno'
d[(1,2)]='Hello world!' #Changes the value associated with key (1,2)
#Values associated with an existing ey are overwritten
#### Adding values to a dictionary
d['five']=5000
#Dictionary are ordered, new pairs are openeded
#At the end of the collection
d.update({6:'six','eight':'hello',9:1890})#here i can put several things
print(len(d)) #Prints the quantity of keys
print(type(d))#Print the type of variable
del d[6]#Deletes the pair with the specified key
temp=d.pop('eight')#removes the pair with specified key
#returns the value associated with the key, and then delet ethe pair.

keys=d.keys()#Returns a view object dict_keys that is iterable
#over the keys of a


values=d.values() #returns a view objec dict_keys that is iterable
#over the vales of d
items=d.items() #returns a view object that is iterable 
#over the pairs odf d (as tuples)

keys_l=list(keys)
items_l=list(items)
values_l=list(values)
              #The first item from each tuple is the key
              #the second item from each tuple is the value
#View objects save memory beccause they do not copy the keys values of pairs,
#they sply allow to 'view' such items form the dictionary indendently
### Iterations over dictionaries
#Dictionaries are ordered (insertion order matters), but not indexed.
#The key are returned in insertion order  
for k in d: #k iterates over each key of d
    print(k,d[k])  #d[k] accesses the value associtaed wit key k
for k in d:
    print(k) #k itereates each key
for k in d.keys(): #iterable view object tje keys of d
    print(k) #k takes each key from d
for v in d.values(): #is iterable
    print(v) #v takes each value from d
    
for t in d.items(): #iterable view object over pairs of d
    print(t) #t is a tuple with each pair from d(k,v)
for k,v in d.items():# Iterable view object over pairs of d
    print(k,v) #k and v are the individual items of previous
    #tuplpe t
    
### Nested dictionaries
d_n={1:'Geeks',2:'For',3:{'A':'Welcome','B':'To','C':'Geeks'}}

d_1={1:['one','two','three'],2:['four','five','six'],3:['seven','eight','nine']}


for k,v in d_1.items():
    print(k,v)
    for i in v:
        print(f'\t{i}')

###Dictionaries vs lists
l_a=['a','b','c','d']
l_r=['d','c','b','a']
d_a={0:'a',1:'b',2:'c',3:'d'}
d_r={3:'d',2:'c',1:'b',0:'a'}
print(l_a[0],d_a[0],l_r[0],d_r[0])
#For the lists,0 is an index
#For the dict, 0 is a key

print(l_a[:2])#sliciing
print(l_r[:2])#sliciing
print(d_a[:2])#sliciing is not available the slice
#slicing is not allowed

###Dictionary comprehension
#Since dictionaries are mutable, we can apply
#a comprehension
#Giventwo lists of th esame size, create a dictionary, where the keys
#are the items from the first list, and the values 
#the items from the second list
lista_1=['a','b','c','d']
lista_2=['Hola',[3,4],(56,4),'Mundo']
d={}
for i in range(len(lista_1)):
    k=lista_1[i]
    v=lista_2[i]
    print(k,v)
    d[k]=v #add a new pair key_value to d
print(d)

#With dict comprehension
d={lista_1[i]:lista_2[i] for i in range(len(lista_1))}

# Nota:
    #los diccionar, al igual que lsos ets, están basados
    #en funciones hash. Esto permite que sean muy eficiente
    #y optimos para la recuperacion (consutla) de informacion
    #Son O(1) para recuperar (consultar/leer) informacion
    #asociada con una llave.
    