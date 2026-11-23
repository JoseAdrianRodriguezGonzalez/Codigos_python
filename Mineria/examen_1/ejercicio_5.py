"""
Nombre: José Adrián Rodríguez González
Curso: Minería de datos
Fecha: 13/10/2025
Descripción: Calculo de la frecuencia en dos variables de titanic
"""
import pandas as pd 
import math
df=pd.read_csv("titanic.csv")
clase=list(df["Pclass"])
embarque=list(df["Embarked"])
tupla=[]
for c,e in zip(clase,embarque):
    if  type(e) is not str:
        continue
    tupla.append((c,e))
clase_val=[elemento[0] for elemento in tupla]
embar_val=[elemento[1] for elemento in tupla]
table={(c,e):0 for c in set(clase_val)
               for e in set(embar_val) }
for clas,emb in zip(clase_val,embar_val):
    table[(clas,emb)]=table.get((clas,emb),0)+1
print(table)
