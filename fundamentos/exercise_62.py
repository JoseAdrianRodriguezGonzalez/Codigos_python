# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:27:01 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Ródriguez González José Adrián
Descripción: Dados dos strings del mismo tamaño (defínelos
tú en el código), escribe un programa que diga cuántos
caracteres se tienen que cambiar para que un string
se convierta en el otro. Convierte los dos strings a
minúsculas antes de las comparaciones.

s1 = 'Hola'
s2 = 'Cola'
output:
    Se tienen que cambiar 1 caracteres para pasar de 'Hola'
	a 'Cola'
    
s1 = 'Pino'
s2 = 'Tono'
output:
    Se tienen que cambiar 2 caracteres para pasar de 'Pino'
	a 'Tono'

"""
s1 = 'Pino'
s2 = 'Tono'
s1=s1.lower()
s2=s2.lower()
cont=0
if len(s1)==len(s2):
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            cont+=1
    print(f'Se tienen que cambiar {cont} caracteres para pasar de {s1} a {s2}')
else:
    print('No')