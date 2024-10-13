# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:58:25 2024

exercise_76

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción: Dada una lista con strings, escribe un programa
usando una comprensión de listas para generar una nueva
lista que incluya aquellos strings que tengan un '.'

lista = ['amor.hy', 'Mundo.tr', 'que.gh', 'tal', 'ala', 'gusto', 'ancho.rt']

output:
    lista_filtrada = ['amor.hy', 'Mundo.tr', 'que.gh', 'ancho.rt']

"""

lista = ['amor.hy', 'Mundo.tr', 'que.gh', 'tal', 'ala', 'gusto', 'ancho.rt']
nueva=[i for i in lista if '.' in i]
print(nueva)