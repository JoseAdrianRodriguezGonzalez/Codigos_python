# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:19:34 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripición: Dados dos diccionarios (definidos por ti),
escribe un programa que genere un tercer diccionario como la mezcla de los 
otros dos. Si hay llaves repetidas, los valores se sobreescriben con los del segund diccionario
d_1={'hola':'a',2:'b',3:'c',5:'h'}
d_2={4:'d',5:'e','hola':'f'}
output:
    {'hola':'f',2:'b',3:'c',4:'d',5:'e'}
"""
d_1={'hola':'a',2:'b',3:'c',5:'h'}
d_2={4:'d',5:'e','hola':'f'}
d_3={}
d_3.update(d_1)
d_3.update(d_2)