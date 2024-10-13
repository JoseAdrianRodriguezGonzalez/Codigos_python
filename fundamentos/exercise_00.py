# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 11:28:01 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción: Escribe un programa que haga la suma de dos números flotantes datos por el usuario. Limita la 
precisión a dos decimales.
input:
    6.7
    7.87
output:
    la suma de los números es 14.50
"""
a,b=float(input('Escribe el primer numero: ')),float(input('Escribe el segundo numero: '))
print(f'La suma de los numeros es: {(a+b):.2f}')