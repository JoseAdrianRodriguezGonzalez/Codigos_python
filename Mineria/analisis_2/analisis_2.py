"""
Description: Para la variable sexo, calcular las frecunecias y porcentajes de cada valor. Imprimir los resultados en orden descendente 
por porcentaje
para graficar

"""
import matplotlib.pyplot as plt
import pandas as pd
from funciones import *
w_d="./"
i_f=w_d+'info_estudiantes.csv'

df=pd.read_csv(i_f)

freq=df["sexo"].tolist()
freq=[i.lower().strip()  for i in freq]
d=conteos(freq)
l_p=sorted([(v/sum(d.values()),v,k) for k,v in d.items()],reverse=False)
print(l_p)
l_f=[f for _,f,_ in l_p]
l_labels=[k for _,_,k in l_p]
# Gráfica de pastel
plt.figure()
plt.pie(l_f,labels=l_labels)

#Gráfico de barras
plt.figure()
plt.bar(l_labels,l_f)
plt.title("Variable sexo")
plt.xlabel("Categorias")
plt.ylabel("Frecuencias")
plt.show()

#####
# EN análisis de datos hay dos artes principales.
#. Los cálculos que permiten encontrar asociaciones,
# # tendencias, patrones.
#2. La interpretación de los cálculos mediant un reporte, un resumen, o una aplicación externa 

# En la interpretación se puede
# incluir hipótesis o especulaciones
#para tratar o explicar sus datos

#¿Porqué tenemos porcentajes similares 
#1. La recolección requería de recopilar la misma cantidad de
#información de hombres y mujeres.
#2. La ingenierías cuenta con más hombres, pero las otras carreras compensan esta diferencia 
#3. Mal captura de datos.


#La 2 se descarte porque solo tenemos un muestreo de la población
#La 3 porque es la más fácil de decidir e inferir, sin embargo, debido a que tenemos la información del muestreo.
# La 1 es más viable y explicativa.
