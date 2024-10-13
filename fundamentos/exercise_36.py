# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:27:48 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Descripcion: Dada una lista de listas (creada por ti) donde cada lista interna 
contiene números  y strings, escribe un programa que genere una nueva lista
a partir de la lista original, pero que contena solo las listas internas con más
de 3 elementos.
list=[[1,2,'s',3],[5,'a'],['h','e','l',45],[4,7,'i']]

"""
lista=[[1,2,'s',3],[5,'a'],['h','e','l',45],[4,7,'i']]
nueva=[]
for i in lista:
    if len(i)>3:
      nueva.append(i)
print(nueva)      

    