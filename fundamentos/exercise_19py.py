# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:38:14 2024

@author: USUARIO
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripcion: Escribe un programa para leer las edades de un grupo d en estudiante ( pide n al usuario
                                                                                   Y calcla laedad promedio)
Limita la salida del promedio a 2 decimales
input:
    Dame cuántos estudianteson :3
    Dame la edad del estudainte 1: 22
    Dame la edad del esutdinate 2:19
        Dame la edad del estudiante 2: 24
output:
    La edad promedio de los etudiantes es 21.67
"""
num= int(input('Escribe la cantidad de alumnos'))
suma=0
for i in range(num):
    edad=int(input(f"Dame la edad del estudiante {i+1}:"))
    suma+=edad
print(f'El promedio de estaturas es de {(suma/num):.2f}')
