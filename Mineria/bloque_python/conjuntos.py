# COnjuntos###

# Colecciónd de elementos que no están rodendos y nose repiten.

# No hay orden -> No están indexados

a=set()
a={1,2,3,4,4}
print(a)

#NO están indexados
#

#Operaciones con conjuntos
#Intersección -> Elementos qeu aparecen en ambos conjuntos
b={'a','b','c',7,8}
c=a.intersection(b)

print(c)

d=a.union(b)

print(d)

e=a.difference(b)

a.add(9)
a.update(['hola','si',2])

a.update({5,6})
print(a)

#Metodo de pop elimina un elemento aleatorio
#metodo remove elimna un elemento deseado

for elemento in b:
    print(elemento)
lista=list(b)
tupla=tuple(b)


#Notas: 
#En cuestión de búsqueda y acceso son ás rápdios que listas o tuplas.
#SOn utiles cuando tnemos elmeneots que no se repiten

#Utilizan tablas hashes para su eficiencia en costo computacional
