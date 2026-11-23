"""
DEscripion: TOmando como base el codigo anterior calcualr la media aritmetica
"""
"""
Hacer una funcion que tome el q1y q3 
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
def outliers(values,q1,q3):
    iqr=q3-q1
    uif=q3+1.5*iqr
    lif=q1-1.5*iqr
    lw=uw=0
    for i in values:
        if i>=lif:
            lw=i
            print("whisker inferior",i)
            break
    for i in values[::-1]:
        if i<=uif:
            uw=i
            print("whisker superior",i)
            break
    outlier=[ v for v in values if v<lw or v>uw]
    return outlier
def recibir(dataframe,variable):
    values=dataframe[variable].tolist()
    s_values=sorted(values)
    five=five_number_summary(s_values)
    print(f'Mínimo: {five[0]:.2f}\nQ1: {five[1]:.2f}\n Q2: {five[2]:.2f}\n Q3: {five[3]:.2f}\n Máximo: {five[4]:.2f}\n')
    #IQR UIF, LIF, whiskers y outliers
    out=outliers(s_values,five[1],five[3])
    print(f"Outliers: ",out,"\n")
    avg=sum(s_values)/len(s_values)
    print(f"promedio: {avg} \n")
    plt.figure()
    plt.boxplot(values)
    plt.title(f"Variable {variable}")
    plt.ylabel(variable)
    #plt.show()
df=pd.read_csv('info_estudiantes.csv')
l_v=['edad','altura','peso','semestre']
for i in l_v:
    recibir(df,i)
    #Mediana es el centro geometrico necesito saber la posicion central entre los datos
#Tanot media como mediana tienen el mismo propósito:
#La media es el centro aritmético, solo necesito sumar dividir para encontrarlo.
##la mediana es el centro geométrico necesito saber la posición para encontrar su valoro
#EL própisto es encontrar un valor típico o esperado que describa el conjunto de datos
#Meidana q2
#media avg
#std