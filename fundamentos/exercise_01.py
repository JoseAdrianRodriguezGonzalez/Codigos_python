# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 11:35:35 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción: Escribe un programa que calcule el promedio de cuatro calificaciones flotantes dadas pro el usiaro.
Al imprimir el promedio, liita la precisión a 2 decimales
input:
    6.7
    7.8
    9.5
    8.9
output:
    El promedio de la calificaciones es 8.23
@author: USUARIO
"""
a,b,c,d=float(input(" ")),float(input(" ")),float(input(" ")),float(input(" "))
print(f'El promedio de la calificaciones es {((a+b+c+d)/4):.2f}')
