# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:19:36 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripición:Escribe un programa que solicite una palabra al usuario, valida que
esté copuesta solo de letras, si no , manda un mensaje de error;
despues devolver un mensaje si la palabra conteien todas las vocales, 
o un mensaj esi no las contiene
input:
    arbol
output:
    no conteien todas las vocales
input murcielago
output:
    'murcielago' conteien todas las letras
    input:
        casa 23
    output:
        no es valida
"""
string =input('Dame una palabra')
if string.isalpha():
    vocale={'a','e','i','o','u'}
    conjunto=set()
    string.lower()
    for i in string:
        if i in vocale:
          conjunto.add(i)  
    if conjunto==vocale:
        print(f'la palabra {string} tiene todas las vocales')
    else:
        print(f'{string} No tiene todas')
else:
    print('Palabra no valida')
