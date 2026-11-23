lista=['d','b','a','a','e','z','z','e']
b=(tuple(set(lista)))
conteo=[lista.count(i) for i in b]
l_freq=sorted(list(zip(conteo,b)),reverse=True)
for k,v in l_freq:
    print(f"{v} en {k}")
