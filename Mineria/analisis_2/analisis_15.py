
"""
Reemplazo
##Correlacion de phi, y probabilidad
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
df=pd.read_csv("info_estudiantes_procesado.csv")

l_v=['sustituir_ia','sexo',"uso_ia"]
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