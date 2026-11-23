#Uso de IA/
"""
Descripcion: Para las variable nominales sexo, uso_ia sustituir_ia y la variable ordinal semestre, calcula las frecuencais y porcentajes de cada
valor,

Imprimir los valores en forma descendente por porcentajes

Hacer n grafico de abarras y uno de pastel
Implementar una función que haga eso
"""
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('info_estudiantes.csv')
def uso_ia_split(element):
    lista=[]
    for i in element:
        if '/' in i:
            l_2=i.split('/')
            if '' in l_2:
                l_2.pop(l_2.index(''))
            lista.extend(l_2)
        else:
            lista.append(i)
    return [i.lower().strip() for i in lista]
def sortCategories(lista):
    d={}
    for elemento in lista:
        d[elemento]=d.get(elemento,0)+1
    l_freq=sorted([(v/sum(d.values()),v,k) for k,v in d.items()])
    return l_freq
freq_g=sortCategories([i.lower().strip()  for i in df['sexo']])
freq_ia=sortCategories(uso_ia_split(df['uso_ia']))
freq_sustituir=sortCategories([ f.strip() for f in df['sustituir_ia']])
freq_seme=sortCategories([ f.strip() if type(f)==str else str(f) for f in df['semestre']])
##
def pieplot(l_data,l_labels):
    plt.figure()
    plt.pie(l_data,labels=l_labels)
    plt.show()
def barplots(data,labels,typeplot):
    plt.figure()
    plt.bar(labels,data)
    plt.title(typeplot)
    plt.xlabel("Categorias")
    plt.ylabel("Frecuencias")
    plt.show()
data_ia=[value for _,value,_ in freq_ia]
labels_ia=[ias for _,_,ias in freq_ia]
def separte(lista):
    values=[values for _,values,_ in lista]
    lables=[label for _,_,label in lista]
    return values,lables
lista_elementos=[separte(freq_ia),separte(freq_g),separte(freq_sustituir),separte(freq_seme)]
titulos=["uso ia","genero","Susituir ia","Semestre"]
for i,j in zip(lista_elementos,titulos):
    pieplot(i[0],i[1])
    barplots(i[0],i[1],j)
    