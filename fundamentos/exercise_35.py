# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:16:28 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Descripción: Dada una lista de números etneros(creada por ti)
escribe un prorama qu genere una nueva lista con aquellos números de la lista 
originial que sean pares y divisible entre 5.
lista=[2,4,5,10,88,20,12,35,46]

"""
lista=[2,4,5,10,88,20,12,35,46]
nueva=[]
for i in lista:
    if i%2==0 and i%5==0:
        nueva.append(i)
print(nueva)
