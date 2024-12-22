# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:00:54 2024
Created on Tue Nov 12 10:52:30 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripcion: Dada una lsita de numeros enteros, escribe un programa usando
funciones lambda que devuelva la lsita interna d emayor longitud y la lsita interna d emenor longitud
lista=[[1,2,3],[2,3],[5,6,7],[8,9,0,1]]
output:
   max:[8, 9, 0, 1]
   min:[2, 3]
"""
lista=[[1,2,3],[2,3],[5,6,7],[8,9,0,1]]
lis_max=max(lista,key=lambda x:len(x))
lis_min=min(lista,key=lambda x:len(x))
print(f'max:{lis_max}')
print(f'min:{lis_min}')