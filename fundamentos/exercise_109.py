# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 00:40:13 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Utilizando el diccionario generado en el
ejercicio previo, devolver una lista con los 3 strings más
frecuentes del diccionario.

d = {'a':3, 'b':2, 'c':1, 'd':2, 'e':1}

output:
    ['a', 'b', 'd']
"""

d = {'a':3, 'b':2, 'c':1, 'd':2, 'e':1}
lista=[v for v in d.values()]
lista.sort(reverse=True)
keys_lista=[]
for k in d.keys():
    for i in lista[:3]:
        if d[k]==i and (k not in keys_lista):
            keys_lista.append(k)

print(keys_lista)