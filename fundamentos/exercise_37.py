# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 11:43:21 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Descripcion:Dada una lista de listas con strings (creada por ti directamente en el código)
escribe un programa qu e'aplane' las listas internas en una nueva lista que 
lista=[['h','e','l'],['l','o],['w','o','r'],['l','d','!']]
output:
    ['h','e','l','l','o','w','o','r','l','d','!']
  """
lista=[['h','e','l'],['l','o'],['w','o','r'],['l','d','!']]
nueva=[]
for i in lista:
    nueva.extend(i)
print(nueva)