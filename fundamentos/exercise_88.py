# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:01:11 2024
exercise_88

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción: Dada una tupla de tuplas, donde cada tupla
interna contiene números flotantes, escribe un programa para
generar una nueva tupla que contenga los promedios de cada
tupla interna.

tupla = ((1.5, 2.5), (3.4, 6.5, 6.1), (1.8, 9.3), (4.5, 5.2, 10.8))

output:
    (2, 5.3, 5.5, 6.8)
"""

tupla = ((1.5, 2.5), (3.4, 6.5, 6.1), (1.8, 9.3), (4.5, 5.2, 10.8))
lista_prom=[]
suma=0
for i in tupla:
    suma=0
    for j in i:
        suma+=j 
    lista_prom.append(suma/len(i))
tupla_prom=tuple(lista_prom)
print(tupla_prom)