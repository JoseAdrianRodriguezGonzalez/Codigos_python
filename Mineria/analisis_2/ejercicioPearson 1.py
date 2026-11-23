"""
Calculr el coeficiente  de correlación de Pearson entre cada par de variable numéricas
edad
peso
altura
semestre
Incluir el rafico de dispersion correspondiente

"""
import matplotlib.pyplot as plt
import pandas as pd

file="info_estudiantes_procesado.csv"
df=pd.read_csv(file)
l_v=["edad","altura","peso","semestre"]
def coeff_pearson(var1,var2):
    var1_mean=sum(var1)/len(var1)
    var2_mean=sum(var2)/len(var2)
    num=0
    den1=0
    den2=0
    for x,y in zip(var1,var2):
        num+=(x-var1_mean)*(y-var2_mean)
        den1+=(x-var1_mean)**2
        den2+=(y-var2_mean)**2
    coeficiente=num/((den1**0.5)*(den2**0.5))
    return coeficiente
def combianciones(l):
    lista=[]
    for variable in enumerate(l):
        lista2=[(variable[1],fur) for fur in l[variable[0]:] if fur!=variable[1] ]
        lista.extend(lista2)
    return lista
print(combianciones(l_v))
def relacion(coef):
    if coef>0.7:
        print("Fuerte")
    elif coef>0.5:
        print("Moderada")
    elif coef>0.3:
        print( "Debil")
    elif coef>0:
        print("casi Nula")
    elif coef==0:
        print("Nula")
    elif coef>-0.3:
        print("Debil negativa")
    elif coef>-0.7:
        print("Moderada negativa")
    else:
        print("Fuerte negativa")
def plot_scatter(x,y,xlabel,ylabel):
    plt.scatter(x,y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(f"Grafico de dispersion {xlabel} vs {ylabel}")
    plt.show()
for var1,var2 in combianciones(l_v):
    coef=coeff_pearson(df[var1],df[var2])
    print(f"Coeficiente de la variable {var1}-{var2}: {coef:.2f}")
    relacion(coef)
    plot_scatter(df[var1],df[var2],var1,var2)
