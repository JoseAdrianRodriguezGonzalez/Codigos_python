"""
DEscripcion: Tomando como ase los ejercicios 12 y 13,hacer lo siguiente:
     Rehacer el código para calcular las estadísticas y graficar los pltos para las avaribales numéicas pero separadas de acuerdor
     a la variable sexo (h/m)
     Omitir el cĺaculo de outliers y bints    
    """
import pandas as pd
import matplotlib.pyplot as plt
name_file='info_estudiantes_procesado.csv'
df = pd.read_csv(name_file)
l_v=['edad','peso','semestre','altura']
#df.boxplot(column='edad', by='sexo')
#df.boxplot(column='semestre', by='sexo')
#df.boxplot(column='altura', by='sexo')
#df.boxplot(column='peso', by='sexo')
#df['edad'].hist( by=df['sexo'], bins=10)
#df['peso'].hist( by=df['sexo'], bins=10)
#df['semestre'].hist( by=df['sexo'], bins=10)
#df['altura'].hist( by=df['sexo'], bins=10)
print(df.groupby('sexo')["edad"].mean())
print(df.corr(""))
#plt.show