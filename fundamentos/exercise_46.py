# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:47:21 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Descripcion:  Dada una lista llena con números y strings
(creada por ti directamente en el código), escribe
un programa que genere una nueva lista que contenga
aquellos elementos que aparezcan al menos 2 veces en la
lista original.

lista = [5, 'a', 'b', 6, 'd', 2, 'a', 'b', 5, 6, 1, 'e']

output:
    [5, 'a', 'b', 6]
"""

lista = [5, 'a', 'b', 6, 'd', 2, 'a', 'b', 5, 6, 1, 'e']
nueva=[]
cont=0
for i in lista:
    if i in nueva:
        continue
    if lista.count(i)>1:
        nueva.append(i)
print(nueva)