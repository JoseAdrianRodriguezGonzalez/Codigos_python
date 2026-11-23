"""
descripcion: Utiliza la tabla de contingencia, hacer una funcion para calcualr los valores esperados
de cada celda de la tabla. 

E_ij = (total_renglon_i*total_renglon_j)/total_n
"""
import pandas as pd
from scipy.stats import chi2
def exp_values(c_v):
    e_v={}
    total=sum(c_v.values())
    total_rc={} #guardar renglon o columna
    chi_square=0
    chi_yate=0
    for t in c_v:
        if t[0] in total_rc:
            r_t=total_rc[t[0]]
        else:
            r_t=sum(v for k,v in c_v.items() if k[0]==t[0])
            total_rc[t[0]]=r_t
        if t[1] in total_rc:
            c_t=total_rc[t[1]]
        else:
            c_t=sum(v for k,v in c_v.items() if k[1]==t[1])
            total_rc[t[1]]=c_t
        e_v[t]=r_t*c_t/total
        chi_square+=(c_v[t]-e_v[t])**2/e_v[t]
        chi_yate+=(abs(c_v[t]-e_v[t])-0.5)**2/e_v[t]
    return e_v,chi_square,chi_yate
def contingencia_tab(v1,v2):
    v_v1=set(v1)
    v_v2=set(v2)
    d_freq={(a,b):0 for a in v_v1
                    for b in v_v2}
    for i,j in zip(v1,v2):
        d_freq[(i,j)]=d_freq.get((i,j),0)+1
    return d_freq
df=pd.read_csv("info_estudiantes_procesado.csv")
l_v=['sexo','sustituir_ia',"uso_ia"]
d_var={v: df[v].tolist() for v in l_v}
d_var['uso_ia']=['s' if v!='n' else v for v in df['uso_ia']]
lista=[]
for variable in enumerate(l_v):
    lista2=[(variable[1],fur) for fur in l_v[variable[0]:] if fur!=variable[1] ]
    lista.extend(lista2)
for var1,var2 in lista:
    df_freq=contingencia_tab(d_var[var1],d_var[var2])
    exp_vals,chi_val,chi_yate=exp_values(df_freq)
    print(chi_val,chi_yate)
    df=1
    print(var1,var2)
    alpha=0.05
#valor de referencia
    ref=chi2.isf(alpha,df)
    if chi_yate>ref:
        print("Se rechaza H0")
        print("SOn independiente")
    else:
        print("se Toma H0")
        print("Existe una dependencia")

