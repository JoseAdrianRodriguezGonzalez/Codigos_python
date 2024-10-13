# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:37:34 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Ródriguez González José Adrián
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
val=s.replace('-','')
lists=[]
if val.isalpha():
   lists=s.split('-')
   lists.sort()
   val='-'.join(lists)
else:
    print('Frase incorrecta')
print(val)