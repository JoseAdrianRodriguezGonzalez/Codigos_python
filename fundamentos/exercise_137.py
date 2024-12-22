# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 10:52:30 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripcion: Dada una lsita de numeros enteros, escribe un programa usando
funciones lambda para generar un anueva lista con los cubos de los numeros de la lsita original
lista=[4,5,1,3]
output:
    [64,125,1,27]
"""
lista=[4,5,1,3]
lista_2=list(map(lambda x:x**3,lista))
print(lista_2)