# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:11:31 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Descripcion: Dadas dos lists llenas con strings (creadas por ti directamente 
 en el código), escribe un programa que devuelva TrueSi tienen al menos un 
elemento en común y Dlase en caso contrario
lista_1=['a','b','c','d']
lista_2=['b','d','e','f','g','h']
output:
    True

"""
lista_1=['a','b','c','d']
lista_2=['b','d','e','f','g','h']

for i in lista_1:
    if (i in lista_2):
        print(True)
        break
else:
    print(False)

