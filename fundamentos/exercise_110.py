# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 10:36:15 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción:Escribe un programa que solicite un sitnrg a usuario, vlaidar que 
esté compuesto solo por letras y que imprima una de las letras
al azar. Si no tiene solo letras,mandar un mensaj de error
'palabra invalidad'
input:
    Dame una palabra: koala
output:
    Un caracter al azar de 'koala' es 'o'
input:
    Dame una palabra: juan45
output:
Juan45 es una palabr ainvaldiad    
"""
import random as rn
string =input('dame una palabra: ')
c=''
if string.isalpha():
    c=rn.choice(string)
    print(f'Un carater al azar de \'{string}\' es \'{c}\'')
else:
    print(f'\'{string}\' es una palabra invalida')