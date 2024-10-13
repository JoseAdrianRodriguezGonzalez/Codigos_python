# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:06:23 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Ródriguez González José Adrián
Descripción: Dado un string (defínelo tú en el código),
que contenga solo letras y espacios, escribe un programa
que determine si el string es un palíndromo (se lee igual
en ambos sentidos). Convertir el string a minúsculas e
ignorar los espacios. Valida que el string solo contenga
letras y espacios, en caso contrario enviar un mensaje que
diga '¡Frase incorrecta!'.

s = 'Anita lava la tina'
output:
    'Anita lava la tina' Es palíndromo
    
s = 'Hola'
output:
    'Hola' No es palíndromo

s = 'Hacia el año 1967, nació'
output:
	¡Frase incorrecta!
	
"""
n=['1','2','3','4','5','6','7','8','9','0']
s = 'Hacia el año 1967, nació'
s=s.replace(' ','')
s=s.lower()
inv=s[::-1]
if s==inv:
    print('Es paliindromo')
elif not(s[::1].isalpha()):
    print('frase incorrecta')
else:
    print('No es palindromo')