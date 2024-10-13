# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:02:00 2024
exercise_90

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción: Dadas dos tuplas del mismo tamaño llenas con
números flotantes, escribe un programa que genere una nueva
tupla que contenga la suma por elemento de las dos tuplas

tupla_1 = (1.5, 6.7, 9.8, 1.4)
tupla_2 = (9.5, 8.5, 1.4, 9.1)

output:
    (11, 15.2, 11.2, 10.5)
"""

tupla_1 = (1.5, 6.7, 9.8, 1.4)
tupla_2 = (9.5, 8.5, 1.4, 9.1)
tupla_suma=()
for i in range(len(tupla_1)):
    tupla_suma=tupla_suma+(tupla_1[i]+tupla_2[i],)
print(tupla_suma)