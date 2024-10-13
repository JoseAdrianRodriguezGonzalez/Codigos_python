# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:34:17 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripcion: Escribe un programa que, con base en una claificaicon entera, 
proporcionada por el usuario hay que validar que sea entre 0 y 10,
indiqe cn una letra la califcacion que le corresponde
10: A
9:B
8:C
7 o 6: D
5 a 0: F
input:
    Dame una califacion:8
output:
    La calificacion es C
"""
calificacion=int(input('Dame una calificacion: '))
if calificacion<=10 and calificacion>=0:
    if calificacion==10:
        print('la calificacion es A')
    elif calificacion ==9:
        print('la calificacion es B')
    elif calificacion ==8:
        print('la calificacion es C')
    elif calificacion ==6 or calificacion ==7:
        print('la calificacion es D')
    else:
        print('F')
else:
    print('Calificacion fuera de rango')
