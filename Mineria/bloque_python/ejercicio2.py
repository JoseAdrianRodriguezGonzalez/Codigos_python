#Ejercicio
lista=['d','b','a','a','e','z','z','e']
d={}
for elemento in lista:
    d[elemento]=d.get(elemento,0)+1
l_freq=[(v,k) for k,v in d.items()]
l_freq.sort(reverse=True)
for v,k in l_freq:
    print(f"{v} veces en {k}")
