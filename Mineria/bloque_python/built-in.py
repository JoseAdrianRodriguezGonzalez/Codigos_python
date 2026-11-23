#FUnción type
#Devuelve el tipo de dato
print(type(6))
print(type("s"))
print(type([1,2]))
# Funciones para números
print(max([1,2,3,4]))
print(min([1,2,3,4]))
print(sum([1,2,3,4]))

print(abs(-1.34))


# Funcines de ordenamiento

#Sorted()

# Regresa una nueva colección de objetos ordenada

lista_o=sorted([0,-1,-2,4,5.3])
print(lista_o)

#Enumerar elementos de una colección
#enumerate
#enumerate(c)
for i,t in enumerate(lista_o):
    print(f"indice{i}, elemento {t}")
#Empaquetar elementos de más de una colección
#zip(c1,c2,c3,c_n)
lista_1=[1,2,3,4,5,6]
lista_2=['a','b','c','d']

for t in zip(lista_1,lista_2):
    print(t)
