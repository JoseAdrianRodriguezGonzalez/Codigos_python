"""
    Procesar el conjunto de datos info_studiantes.csv directamente con pandas
"""
import pandas as pd
name_file='info_estudiantes.csv'
df=pd.read_csv(name_file)
print(df.info())
#print(df["sustituir_ia"].unique())
# Sexo
df['sexo']=df['sexo'].str.lower()
df['sexo'] =df['sexo'].str.strip()
print(df["sexo"].unique())
#Sustituir IA
df['sustituir_ia'] =df['sustituir_ia'].str.strip()
print(df["sustituir_ia"].unique())
#Opciones
print(df['uso_ia'])
df['uso_ia'] =df['uso_ia'].str.lower()
print(df['uso_ia'].unique())
uso_ia =df['uso_ia'].to_list()
unique=('chatgpt','gemini','copilot','otro','n')        
uso_ia_procesado=[]
for val in uso_ia:
    if val[-1]=='/':
        val=val[:-1]
    comb=set([t if t in unique else "otro" for t in set(val.split('/')) ])
    print(comb)
    uso_ia_procesado.append('/'.join(comb)) 
df['uso_ia']=uso_ia_procesado
df.to_csv('info_estudiantes_procesado.csv',index=False)