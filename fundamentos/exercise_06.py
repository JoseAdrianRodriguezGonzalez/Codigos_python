# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 11:04:56 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripcion: Escribe un programa que calcule la distnacia Euclidian entre
dos puntos en el plano carteison, dadas las coordenadas de los dos puntos.
Limtia la precisión a 3 decimales
input :
    Dame el valor x del punto 1:
    Dame el valor y del punto 1:
    Dame el valor x del punto 2:
    Dame el valor y de punto 2:
"""
x1=float(input('Dame el valor x del punto 1: '))
y1=float(input('Dame el valor y del punto 1: '))
x2=float(input('Dame el valor x del punto 2: '))
y2=float(input('Dame el valor y del punto 2: '))
distancia=((x2-x1)**2+(y2-y1)**2)**(1/2)
print(f'La distancia Euclideana entre los dos puntos es {distancia:.2f}')
    