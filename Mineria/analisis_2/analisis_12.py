"""
Created on thu
Tomando como base el ejercicio previo.
Hcer una función que tome una lista de dato ordenada y la separe ne n bins (n es definida pro el suuario )
Encontrar los límites inferiores y superiores de cada bin

ESta función se llama dentro ed l función resmuen
"""
"""
@Desciription: Tomando como base el ejercicio 8, escribir una función que calcule la varianza, la desviación estándar e imrima el coeiciente de variabildad.

"""

import pandas as pd
import matplotlib.pyplot as plt
def get_bins(values,n_bins=5):
    maximo=values[-1]
    minimo=values[0]
    rango=maximo-minimo
    size=rango/n_bins
    steps=[(minimo+i*size,minimo+(i+1)*size) for i in range(n_bins)]
    
    #for inf_b,sup_b in steps[:-2]:
    #    temp=[]
    #    for v in values:
    #        if (v>=inf_b and v<sup_b):
    #          temp.append(v)
    #        if sup_b==maximo and v==sup_b:
    #            temp.append(v)
    #    bins.append(temp)  
    ## Forma 3
    lim_sup=minimo+size
    bins=[[]]
    stages=0
    for v in values:
        if v>=lim_sup and stages<n_bins-1: 
            stages+=1
            lim_sup+=size
            bins.append([])
        if v<lim_sup or stages==n_bins-1:
            bins[stages].append(v)   
        
            
    return steps,bins
           
def varianza(values):
    n=len(values)
    avg=sum(values)/n
    var=sum([(val-avg)**2 for val in values ])/(n-1)
    std=var**(1/2)
    return var,std
def cuartil(values,q):
    p_q=q*(len(values)-1)/4 
    k=int(p_q)
    val=values[k]+(p_q-k)*(values[k+1]-values[k])
    return val
def five_number_summary(values):
    return values[0],cuartil(values,1),cuartil(values,2),cuartil(values,3),values[-1] 
def trim_data(values,p=5):
    """Ya ordenados"""
    n=len(values)
    k=int(p*n/100)
    return values[k:n-k]
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
   # s_values=trim_data(s_values)
    five=five_number_summary(s_values)
    print(f'Mínimo: {five[0]:.2f}\nQ1: {five[1]:.2f}\n Q2: {five[2]:.2f}\n Q3: {five[3]:.2f}\n Máximo: {five[4]:.2f}\n')
    #IQR UIF, LIF, whiskers y outliers
    out=outliers(s_values,five[1],five[3])
    print(f"Outliers: ",out,"\n")
    avg=sum(s_values)/(len(s_values))
    _,std=varianza(s_values)
    cv=std/avg
    print(f"std:{std}")
    print(f"CV:{cv}")
    print(f"promedio: {avg} \n")
    #BIns paa generar histograma
    lista,bins=get_bins(s_values,n_bins=5)
    print(lista)
    print(bins)
   # plt.hist(s_values,bins=10)
   # plt.title(f"Variable {variable}")
   # plt.xlabel("Frecuencias")
   # plt.show()
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



#Notas:
#Diferente número de bins va a producir un cambio en la distribución
#Cambiando la distribución se Revelan diferentes propiedades
#de los datos (brechas o posibles outliers)
#NO hay un número de bins qu ¿e sea el adecuado o el perfecto,
# EN general, las variables de estatura,peso y edad se aproximan a una distribución normal

#Por otro lado, la variable semestre se aproxima a una distribución uniforme