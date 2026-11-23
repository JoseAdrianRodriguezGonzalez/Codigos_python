"""

DEscription: Más sobre pandas
"""
import pandas as pd 
import matplotlib.pyplot as plt
#Archivo en forma de DataFrame
df=pd.read_csv('info_estudiantes.csv')
print(df)


#Slicing 
#INICIO: FINAL-1
print(df[0:3])
print(df[0:10:50])

### FUnciones ###
#describe()
#REsume las columnas que sean númericas 
#proporcionando el número de registros, la media, std, deb, el resume de los 5 números
print(df.describe())

#SObre una columna
print(df["edad"].describe())
#Dos columnas o más
print(df[:10][["edad","altura"]].describe())

#Diagrama de caja
#agrupar
df.boxplot()

#desagrupar
df[["edad"]].boxplot()

# EStadísticas individualmente
# Media
print(df["edad"].mean())
print(df["edad"].median())
print(df["edad"].quantile(q=0.25))
#Dos o másvariables
#También se puede aplicar un slicing
print(df[["edad","altura"]].quantile(q=0.25))
# Método de ordenamiento
#.sort_values(by=variable)
# Regresar un nuvo datarame ordenado
df_sorted=df.sort_values(by="edad",ascending=False)
#También se puede aplicar slicing
print(df_sorted)   
#FIltros##
#FIltrar las observaciones ed acuerdo a una o más condiciones
#Regresa un tipo de dato Series, conteniendo valores Flase y True
filtro_edad=(df["edad"]>23)
print(df[filtro_edad]["edad"])
# Personas con una edad mayor a 23 y qque sean mujeres
filtro_edad=(df["edad"]>23 )| (df["sexo"]=="m")
print(df[filtro_edad])

##FIltro semestre
filtro_semestre=(df["semestre"]>9)&(df["sexo"]=="h")
print(df[filtro_semestre])

#Filtrado de acuerdo a substrings
filtro_gpt=(df["uso_ia"].str.contains("gemini"))
print(df[filtro_gpt]["uso_ia"])
print(df[filtro_gpt].describe())

#Agrupar nuevamente después del fitlrdo+
df[filtro_gpt].boxplot(column="edad",by="sexo")
##Gráficos de dispersión
df[filtro_gpt].plot(x="edad",y="semestre",kind="scatter")
df.hist(bins=6)
df[filtro_gpt][["edad"]].hist()
#generar histogramas agrupados
df[filtro_gpt][["edad","altura"]].hist(bins=5,by=df["sexo"])
#COnteo de vlaores nulos o NaN
print(df.isnull().sum())

#Registros duplciados
print(df.duplicated().sum())
#ELiminar registro duplicados
df_procesed=df.drop_duplicates()
#Eliminar registros donde exista n valor nulo
df_processed=df.dropna(subset=["edad"]) #EL subset indica la variale que elimina las ocurrencias que hayan errores 
#Llenar atributos de registros eonde exista un
df['sexo']=df['sexo'].fillna(12)