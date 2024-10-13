# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:37:17 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Dada una lista llena con strings escribe un programa que genere una nueva lista con los elementos
unicos de la lista original(i.e una lista sin elementos duplicados)
lista=['a','b','c','a','a','b','d']
output:
    ['a','b','c','d']
"""
lista=['a','b','c','a','a','b','d']
nueva=[]
for i in lista:
    if (i not in nueva):
        nueva.append(i)
    