"""
Tomando como base el ejercicio para generar lat abla de contingencia entre un var de variables, hacer lo siguiente:
-INcluir la función que calcule el coeficiente ed correlacion de phi

    """
import pandas as pd
def contingencia_tab(v1,v2):
    v_v1=set(v1)
    v_v2=set(v2)
    d_freq={(a,b):0 for a in v_v1
                    for b in v_v2}
    for i,j in zip(v1,v2):
        d_freq[(i,j)]=d_freq.get((i,j),0)+1
    return d_freq
def coeff_phi(var1,var2):
    tabla=contingencia_tab(var1,var2)
    l_keys=sorted(list(tabla.keys()))
    print(l_keys)
    n_00=tabla[l_keys[0]]
    n_01=tabla[l_keys[1]]
    n_10=tabla[l_keys[2]]
    n_11=tabla[l_keys[3]]
    n_1=n_11+n_01
    n_0=n_10+n_00
    n1_=n_11+n_10
    n0_=n_01+n_00
    print(n_1,n_0,n1_,n0_)
    coeff=((n_11*n_00)-(n_10*n_01))/(n_1*n_0*n1_*n0_)**(1/2)
    return coeff
df=pd.read_csv("info_estudiantes_procesado.csv")

l_v=['sexo','sustituir_ia',"uso_ia"]
d_var={v: df[v].tolist() for v in l_v}
d_var['uso_ia']=['s' if v!='n' else v for v in df['uso_ia']]
lista=[]
for variable in enumerate(l_v):
    lista2=[(variable[1],fur) for fur in l_v[variable[0]:] if fur!=variable[1] ]
    lista.extend(lista2)
for var1,var2 in lista:
    print(var1,var2)
    df_freq=contingencia_tab(d_var[var1],d_var[var2])
    print(df_freq)
    coeff=coeff_phi(d_var[var2],d_var[var1])
    print(coeff)