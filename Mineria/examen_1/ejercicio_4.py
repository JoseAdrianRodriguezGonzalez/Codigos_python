"""
Nombre: José Adrián Rodríguez González
Curso: Minería de datos
Fecha: 13/10/2025
Descripción: Calculo de correlacion
"""

import pandas as pd
import math
df=pd.read_csv("student.csv",delimiter=";")
abse=df["absences"]
g=list(df["G3"])
tupla=[]
for a,g_ in zip(abse,g):
    if math.isnan(a) or math.isnan(g_):
        continue
    tupla.append((a,g_))
absences=[elemento[0] for elemento in tupla]
g3=[elemento[1] for elemento in tupla]
def media(valores):
    return sum(valores)/len(valores)
def correlacion(var1,var2):
    mux=media(var1)
    muy=media(var2)
    cov=sum([(x-mux)*(y-muy) for x,y in zip(var1,var2)])
    varx=sum([(x-mux)**2 for x in var1])**0.5
    vary=sum([(y-muy)**2 for y in var2])**0.5
    return cov/(varx*vary)
print(f"la correlacion de ambas variables es de {correlacion(absences,g3)}")
