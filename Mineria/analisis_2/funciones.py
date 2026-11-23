import pandas as pd
def conteos(lista):
    d={}
    for elemento in lista:
        d[elemento]=d.get(elemento,0)+1
    return d
def frecuencias(dicti):
    d={}
    for k,v in dicti.items():
        d[k]=v/sum(dict.values())
    return d
