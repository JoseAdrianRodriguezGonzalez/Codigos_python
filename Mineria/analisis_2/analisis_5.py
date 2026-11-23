"""

@Description: Para cada variable de intervalo/razón:
edad, altura, peso y la variable peso
Hacer una función que reciba el dataframe y e l nombre de la variable a analziar

Obtener un gráfico de dispersión natural y uno ordenado
"""
import pandas as pd
import matplotlib.pyplot as plt
def recibir(dataframe,variable):
    values=dataframe[variable].tolist()


    #graficos
    plt.figure()
    plt.scatter(range(len(values)),values)
    plt.ylabel(variable)
    plt.title(f'Variable {variable} no ordenada')
 #   plt.savefig('plots/{var}_scatter_natural.png')
    plt.show()
    #Gráficos dispersión ordenada
    s_values=sorted(values)
    plt.scatter(range(len(s_values)),s_values)
    plt.ylabel(variable)
    plt.title(f'Variable {variable} ordenada')
    plt.show()
#    plt.savefig('plots/{var}_scatter_ordenado.png')

    return


df=pd.read_csv('info_estudiantes.csv')
l_v=['edad','altura','peso','semestre']
for i in l_v:
    recibir(df,i)