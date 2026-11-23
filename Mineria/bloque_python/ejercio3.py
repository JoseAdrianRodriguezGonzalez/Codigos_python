#Ejercicio
#Obtener las frecuenias de los numros dentro la lista.

lista=[1,1,1,0,0,0,0,112,2,2,100,100,100]
d={}
dire='./../data/'
name=dire+'frecuencias.txt'
for elemento in lista:
    d[elemento]=d.get(elemento,0)+1
l_freq=[(v,k) for k,v in d.items()]
l_freq.sort(reverse=True)
with open(name,'w',encoding='utf-8')as file:
    for v,k in l_freq:
        file.write(f'{v}:{k}\n')

