# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:42:22 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Ródriguez González José Adrián
Descripción: Dada una lista llena con strings (creada por
ti directamente en el código), escribe un programa que
genere otra lista con los strings que tengan una longitud
mayor a n (número entero definido por ti en el código).

lista = ['merequetengue', 'hola', 'que', 'tal', 'mundo']
n = 4

output:
    ['merequetengue', 'mundo']
"""

lista = ['merequetengue', 'hola', 'que', 'tal', 'mundo']
n = 4
nueva=[]
for i in lista:
    if len(i)>n:
        nueva.append(i)
print(nueva)