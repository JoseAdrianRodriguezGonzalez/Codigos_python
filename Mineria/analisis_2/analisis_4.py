"""
@Descripción : TOmando como ase el ejercicio anterior, las variables nominales y la variables numérica de peso a una variable ordinal.

Para la variable de peso calcular las frecuencias y porcentajes en los rangos [0-50],[50,60],[60-70],[70-80],[80+]
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('info_estudiantes.csv')
peso=df['peso']
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
def separte(lista):
    values=[values for _,values,_ in lista]
    lables=[label for _,_,label in lista]
    return values,lables
def conteos(lista):
    d={}
    for elemento in lista:
        print(elemento)
        if elemento<=50:
            d['0-50']=d.get('0-50',0)+1
        elif elemento<=60:
            d['50-60']=d.get('50-60',0)+1
        elif elemento<=70:
            d['60-70']=d.get('60-70',0)+1
        elif elemento<=80:
            d['70-80']=d.get('70-80',0)+1
        else:
            d['80+']=d.get('80+',0)+1
    l_freq=sorted([(v/sum(d.values()),v,k) for k,v in d.items()])
    return l_freq
def frecuencias(dicti):
    d={}
    for k,v in dicti.items():
        d[k]=v/sum(dict.values())
    return d
def sortCategories(lista):
    d={}
    for elemento in lista:
        d[elemento]=d.get(elemento,0)+1
    l_freq=sorted([(v/sum(d.values()),v,k) for k,v in d.items()])
    return l_freq
freq_seme=sortCategories([ f.strip() if type(f)==str else str(f) for f in df['semestre']])
freq_peso=conteos(peso)

lista_elementos=[separte(freq_peso),separte(freq_seme)]
titulos=["peso","Semestre"]
for i,j in zip(lista_elementos,titulos):
    pieplot(i[0],i[1])
    barplots(i[0],i[1],j)