# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:01:25 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Ródriguez González José Adrián
Descripción: Dado un string (defínelo tú en el código),
escribe un programa que devuelva cuántas veces aparece el
string 'bob' dentro de él.

s= 'bobobbob bob'

output:
    'bob' parece 4 veces
"""

s= 'bobobbob bob'
cont=0
for i in range(len(s)-3):
    if s[i:i+3] =='bob':
        cont+=1
print(f'bob aparece {cont}')