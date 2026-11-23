"""

@Description: Calcular los 4 números
INcluvir el diagrama de boxplot
"""
import pandas as pd
import matplotlib.pyplot as plt
def cuartil(values,q):
    p_q=q*(len(values)-1)/4 
    k=int(p_q)
    val=values[k]+(p_q-k)*(values[k+1]-values[k])
    return val
def five_number_summary(values):
    return values[0],cuartil(values,1),cuartil(values,2),cuartil(values,3),values[-1]
def recibir(dataframe,variable):
    values=dataframe[variable].tolist()
    s_values=sorted(values)
    five=five_number_summary(s_values)
    print(f'Mínimo: {five[0]:.2f}\nQ1: {five[1]:.2f}\n Q2: {five[2]:.2f}\n Q3: {five[3]:.2f}\n Máximo: {five[4]:.2f}\n')
    plt.figure()
    plt.boxplot(values)
    plt.title(f"Variable {variable}")
    plt.ylabel(variable)
    plt.show()
df=pd.read_csv('info_estudiantes.csv')
l_v=['edad','altura','peso','semestre']
for i in l_v:
    recibir(df,i)