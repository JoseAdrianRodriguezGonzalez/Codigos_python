# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:21:36 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripición: Escribe un programa usando una comprehension list, para generar
 una lista llena con los numeros al cuadrado entre uno y mil
 output:
     [1,4,9,16,25,36...]
"""
lista=[x**2 for x in range(1,1001)]

print(lista)