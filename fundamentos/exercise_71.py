# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:25:39 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripición: Escribe un programa usando  una comprehension lsit para generar 
una lista llena con los numeros pares divisble entre 5 que estén entre 1 y 1000:
    output:
        [10,20,30,...]
"""

lista=[x for x in range(1,1001) if not(x%2) and not(x%5)]
print(lista)