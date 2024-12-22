# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 23:39:52 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Dados dos diccionarios con llaves string y
valores strings y números, escribe un programa que genere un
tercer diccionario como la mezcla de los otros dos. Si hay
llaves repetidas, que sume los valores que sean numéricos,
si son strings, que los concatene, si son diferentes, que se sobreescriban.

d_1 = {'a':'hola', 'b':5, 'c':7, 'd':'que'}
d_2 = {'d':'mundo', 'a':8, 'b':7}

output:
    d_3 = {'a':8, 'b':12, 'c':7, 'd':'quemundo'}
"""


d_1 = {'a':'hola', 'b':5, 'c':7, 'd':'que'}
d_2 = {'d':'mundo', 'a':8, 'b':7}
d_3=d_1.copy()
for i, j in d_2.items():
    if i in d_3.keys():

        if type(j)==str and type(d_3[i])==str:
            d_3[i]=d_3[i]+j
            continue
    
        elif (type(j)==int or type(j)==float) and (type(d_3[i])==int or type(d_3[i])==float) :
            d_3[i]+=j
            continue
        else:
            d_3[i]=j
            