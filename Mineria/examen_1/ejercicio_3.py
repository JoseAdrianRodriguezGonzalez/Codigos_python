"""
Nombre: José Adrián Rodríguez González
Curso: Minería de datos
Fecha: 13/10/2025
Descripción: Programa que calcula las desviaciones y las medias
"""

import pandas as pd
import math
df=pd.read_csv("student.csv",delimiter=";")
edad=df["age"]
sex=list(df["sex"])
tupla=[]
for e,s in zip(edad,sex):
    if math.isnan(e):
        continue
    tupla.append((e,s))
def media(valores):
    return(sum(valores)/len(valores))
def std(valores):
    mu=media(valores)
    std=sum([(v-mu)**2 for v in valores])/(len(valores)-1)
    return std**0.5
def cuartil(valores,nq):
    n=len(valores)
    pq=(n-1)*nq/4
    pq_index=int(pq)
    valor=valores[pq_index]+(pq-pq_index)*(valores[pq_index+1]-valores[pq_index])
    return valor
def five_numbers(valores):
    s=sorted(valores)
    minimo=s[0]
    maximo=s[-1]
    q1=cuartil(s,1)
    q2=cuartil(s,2)
    q3=cuartil(s,3)
    return minimo,q1,q2,q3,maximo

female_ages=[elemento[0] for elemento in tupla if elemento[1]=="F"]

male_ages=[elemento[0] for elemento in tupla if elemento[1]=="M"]


print(f"Desviacion estandar de las edades de las mujeres {std(female_ages)}")
print(f"Media de las edades de las mujeres {media(female_ages)}")
print(f"El resumen de los 5 numeros de las mujeres es {five_numbers(female_ages)}")
print(f"Desviacion estandar de las edades de los hombres {std(male_ages)}")
print(f"Media de las edades de los hombres {media(male_ages)}")

print(f"El resumen de los 5 numeros de las mujeres es {five_numbers(male_ages)}")
