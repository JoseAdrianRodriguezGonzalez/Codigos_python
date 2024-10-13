# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:39:56 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripición: Dada una lsita de listas, exscribe un programa usando una comrpension de listas
para crear una nueva lsita ue contenga 
la longitud de cada string de la lista original
lista=['Hola','Mundo','que','tal','mucho','gusto']
output:
    [4,5,3,3,5,5]
"""

lista=['Hola','Mundo','que','tal','mucho','gusto']
longitudes=[len(x) for x in lista ]
print(longitudes)