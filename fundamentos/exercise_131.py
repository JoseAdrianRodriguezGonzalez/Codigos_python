# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 10:38:08 2024

@author: USUARIO
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Escribe una función que reiba una lsita de string, y que decule va una lsita
de tplas, cada tupla deve contener 2 elementos
el primero e sla posicion de cada sitrng y el segundo e sel string.
lsita=['a','b','c','d']
output:
    [(0,'a'),(1,'b'),(2,'c'),(3,'d')]

"""
lista=['a','b','c','d']

def lista_tuplas(lista):
    return [o for o in enumerate(lista)]
lista_nueva=lista_tuplas(lista)
print(lista_nueva)