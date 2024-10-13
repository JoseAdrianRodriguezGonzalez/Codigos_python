# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 10:45:16 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripición: Dada una lista de strings, escribe un programa usando una comrpension de listas
para crear una nueva lsita ue contenga 
solo los string de la lista originalq eu incien con una 'a'
lista=['amor','Mundo','que','tal','Ala','Ancho','gusto']
output:
    [4,5,3,3,5,5]
"""
lista=['amor','Mundo','que','tal','Ala','Ancho','gusto']

palabras=[c for c in lista if not(c.lower().find('a'))]
print(palabras)