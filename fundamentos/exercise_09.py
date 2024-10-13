# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 10:46:04 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción: Escribe un programa que calcule el valor absoluto de un número
flotante dado por el usuario (sin usar funciones).
input:
    Dame un número : -5.2
    Dame un número : 8
output:
    El valor absoluto es: 5.2
    El valor absoluto es: 8
"""
num=float(input('Dame un numero: '))
if(num>=0):
    print(num)
else:
    print(f'el valor absoluto es: {-num}')