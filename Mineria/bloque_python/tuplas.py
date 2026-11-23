"""
Tuplas
"""

#### Tuplas #####
#COlección ordenada de objetos 

# SE puede acceder a sus elmentos mediantes indices.

#No es mutable

tupla=()

tupla=("Tupleas","son","como","listas",1,2,[3,5.8])

print(tupla[0])
print(tupla[-1])

t2=tupla+(1,2,3)

t3=tupla+(1,)

t4=t3[:4]+t3[5:]
print(t3)
print(t4)

#Si la elimnación o inserción de elementos e s recuentes, pues no es recomendable usa runa tupla

# Casting

lista=list(t4)
tupla=tuple(t4)

# Funciones 
# index(val)
#print(t4.index('hola'))

t5=t4*3
 
print(t4.count('hola'))



# Desempaquetamiento de tuplas

t=('a','b','c')
# DEbe de haber una equivalencia
v1,v2,v3=t
for elemento in tupla:
    print(elmento)

# Notas: el acceso es más rápido que en las listas

#Son útiles cuando la colección de objetos nunca va a cambiar 
#Nunca comenzar con una tupla vacía 
