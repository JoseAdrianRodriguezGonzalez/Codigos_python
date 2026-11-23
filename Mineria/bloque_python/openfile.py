w_d="./data/"
o_f=w_d+"numero.txt"

with open(o_f,'a+',encoding='utf-8')as file:
    for i in range(10):
        file.write(f'{i*i}\n')
with open(o_f,'r',encoding='utf-8') as file:
    for i in file:
        temp=i.strip()
        print(temp)
#Ejercicio
#Obtener las frecuenias de los numros dentro la lista.

lista=[1,1,1,0,0,0,0,112,2,2,100,100,100]
d={}
for elemento in lista:
    d[elemento]=d.get(elemento,0)+1
l_freq=[(v,k) for k,v in d.items()]
l_freq.sort(reverse=True)
for v,k in l_freq:
    
