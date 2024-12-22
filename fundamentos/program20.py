# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:25:31 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: José Adrián Rodríguez González
Descripcion: More about pandas
"""
import pandas as pd

f_path="C:/Users/USUARIO/Documents/Universidad/terer/fundamentos/code/data/"
f_name="info_students"
f_extension='.csv'
file=f_path+f_name+f_extension
df=pd.read_csv(file)

#Statistics methods
print(df.describe())
#Reutrns some statistics about the numeric data
print(df[['age','weight']].describe())
df.hist()
df[['age','semester']].hist(bins=2)##
df.boxplot(column='semester')
age_mean=df['age'].mean()#scalar
age_median=df['age'].median()#scalar

print(df[['age','height']].mean())#series

print(df[['age','height']].median())#series
print(df[['age','height']].quantile(0.25))###series

###Comparadores filtros
print(df['age'])
print(df['age']>21) ##Va a aplicar el comparador a cada elemento de la columna y devuelve un valor booleano 
#para cada resultado 


age_filter=(df['age']>21)
print(df[age_filter])
##Devuelve aquellos valores en los es verdadero

sex_filter=(df['sex']=='m')
print(df[sex_filter])

print(df[sex_filter].sort_values(by='age'))##primero filtra el dataframe
#luego lo ordena de menor a mayor por la edad


###Devuelve un data frame

##Mas sobre filtos

sex_console_filter=((df['game_console']=='y') & (df['sex']=='m'))
#Retrusn students that have console and are women
#& --> and for pandas

print(df[sex_console_filter])
sex_console_filter=((df['game_console']=='y') | (df['sex']=='m'))
#Returns students that have console or ar ewomen
### | ->
print(df[sex_console_filter])

console_filter=(df['game_console']=='y')
print(df[sex_console_filter].describe())
df[sex_console_filter][['weight']].boxplot()

df[console_filter].boxplot(column='weight',by='sex')


##Count values
df.count()# Count the number of non NaN values in eaxh column
df['sex'].count()
df['sex'].value_counts()#Count the number of unique values in column
df['semester'].value_counts()

##Arithmetic operations
print(df['age']/df['height'])
#element wise
print((df['age']+3)/(df['height']+1))
#Precedencia de los operadores:
#izquierda a derecha cuando son ARITMETICOS, los LÓGICOS son los que se hacen de derecha a izquierda


##Group by
#A groupby operation involves some combination of splitting the data, applying a function, and combining the results.

groups=df.groupby('sex')
#crea tantos grupos como valores que tneg ala llave
#--> groups es un objeto iterale que liga con los datos de cada grupo.
for group in groups:
    print(group)
#Cada grupo es una tupla con dos items
#El primer item es para el valor del grupo 
#El segundo es para cada valor dentro de ese dataframe

for name,group in groups:
    print(name)
    print(group['age'].mean())
    # Mean for age for each group
groups.get_group('h') #Get the df associated with group
groups.get_group('h').describe()

#Coomon use
df.groupby('sex')[['age']].mean()


####Sorting results
#By default, the results of the functions applied on groups are sorted in descending order.
#
df.groupby('sex',sort=False)[['age']].mean()
#when sort=Flase, sortin is deactivated and the results are shonw in the order 
#in the which the values for the k (sex) appear
df.groupby('sex')[['age','height']].mean()
#Mean of age height grouped by sex
df.groupby(['sex','game_console'])[['age']].mean()
#Menan of age grouped first by sex and then by game console
#Se agrupa la primera caracteristica, (hombres y mujeres) y luego los que tienen o no consola
df.groupby(['sex','game_console'])[['age','height']].mean()

##Using filter

df[sex_filter].groupby('game_console')[['age']].mean()
df.groupby('sex')[['age']].describe()
#Statistics for age group by sex
df.groupby('sex')[['age','height']].describe()



#Statistics for ae and hegt grouped by sex

df[sex_filter].groupby('game_console')[['age']].describe()
df[sex_filter].groupby('game_console')[['age','height']].describe()
#Statistics for age and height for women grouped by consoles
###PLots
df.groupby('sex').boxplot()
df.groupby('sex')[['age']].boxplot()


##Boxplots for age and semestser grouped by sex
df[sex_filter].groupby('game_console')[['age']].boxplot()
#Boxplots for age for women, grouped by console
df[sex_filter].groupby('game_console')[['age','semester']].boxplot()

##One-hot encoding
df_encoded=pd.get_dummies(df,columns=['sex'])






