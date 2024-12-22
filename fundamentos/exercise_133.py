# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:02:47 2024


@author: USUARIO
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Escribe una función que recibda dos listas de strings del mismo tamaño, y que devuelva un diccionario en done las llaves
son los stirng de la primera lsita, y los valores delos stirngs de la segunda lista.
colores=['azul','negro','rosa','amarillo']
colors=['blue','black','pink','yellow']
        output:
            {'azul':'blue','negro':'black','rosa':'pink','amarillo':'yellow'
"""

colores=['azul','negro','rosa','amarillo']
colors=['blue','black','pink','yellow']
def diccionario(lista_1,lista_2):
    return dict(zip(lista_1,lista_2))
diccionario_1=diccionario(colores, colors)
print(diccionario_1)
