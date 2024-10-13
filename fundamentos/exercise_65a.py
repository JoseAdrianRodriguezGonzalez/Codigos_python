# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:02:42 2024

exercise_65

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodrígeuz González José Adrián
Descripción: Dado un string (defínelo tú en el código)
compuesto por palabras separadas por un '-', escribe un
programa que genere otro string con las mismas palabras
separadas por '-', pero ordenadas alfabeticamente. Valida
que el string original solo contenga letras y el caracter
'-', en caso contrario, manda un mensaje que diga 
'¡Frase incorrecta!'.

s = 'anita-lava-tina-mucho-esfuerzo'
output:
    'anita-esfuerzo-lava-mucho-tina'
    """
s = 'anita-lava-tina-mucho-esfuerzo'
s_val1=s.split('-')
s_val2=''.join(s_val1)
if s_val2.isalpha():
    s_val1.sort()
    s_val1='-'.join(s_val1)
    print(s_val1)
else:
    print('¡Frase incorrecta!')