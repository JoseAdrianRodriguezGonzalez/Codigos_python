"""
Nombre: José Adrián Rodríguez González
Curso: Minería de datos
Fecha: 13/10/2025
Descripción: Programa que cuenta los estudiantes"""

import pandas as pd
df=pd.read_csv("student.csv",delimiter=";")
status=list(df["Pstatus"])
sexo=list(df["sex"])
frecuencia_mujeres_padres=0
#Frecuencia de mujeres con ambos padres
frecuencia_hombres_padres=0
frecuencia_juntos=0
frecuencia_separado=0
frecuencia_mujeres_padre=0
frecuencia_hombres_padre=0

for stato,sexo in zip(status,sexo):
    if sexo=="F" and stato=="T":
        frecuencia_mujeres_padres+=1
    elif sexo=="M" and stato=="T":
        frecuencia_hombres_padres+=1 
    if stato=="T":
        frecuencia_juntos+=1   
    if sexo=="M" and stato=="A":
        frecuencia_hombres_padre+=1
    if sexo=="F" and stato=="A":
        frecuencia_mujeres_padre+=1
    if stato=="A":
        frecuencia_separado+=1

#Frecuencia de estudiantes juntos
print(f"Cuanto estudinates viven con ambos padres: {frecuencia_juntos}")
print(f"Cuantas mujeres viven con ambos padres: {frecuencia_mujeres_padres}")
print(f"Cuanto hombres viven con ambos padres {frecuencia_hombres_padres}")
print(f"Cuanto estudinates viven con un unico padre{frecuencia_separado}")
print(f"Cuantas mujeres viven con un uncio padre{frecuencia_mujeres_padre}")
print(f"Cuantas hombres viven con un uncio padre: {frecuencia_hombres_padre}")
