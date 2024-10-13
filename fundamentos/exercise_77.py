# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 18:59:05 2024

exercise_77

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción: Dada una lista con strings, escribe un programa
usando una comprensión de listas para generar una nueva
lista que incluya aquellos strings que terminen en las
extensiones '.jpg' o '.png'

lista = ['amor.hy', 'Mundo.jpg', 'que.ghtg', 'tal.png',
		'ala.png', 'gusto', 'ancho.rty', 'pelota.png',
		'juego.png.thx']

output:
    lista_filtrada = ['Mundo.jpg', 'tal.png', 'ala.png',
					'pelota.png']
"""


lista = ['amor.hy', 'Mundo.jpg', 'que.ghtg', 'tal.png',
		'ala.png', 'gusto', 'ancho.rty', 'pelota.png',
		'juego.png.thx']
nueva=[i for i in lista if ('.png' in i[-4:]) or('.jpg' in i[-4:])]
print(nueva)