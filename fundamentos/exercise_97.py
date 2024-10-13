# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 11:38:36 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripición:Escribe un programa que solicite una palabra al usuario, valida que
esté compuesta solo de letras, si no , manda un mensaje de error;conviertela
a minusculas y que despues devuelva un mensaje si la palabra es un heterograma (o no lo es)
Un heterograma es una palabra que cada palabra solo ocurre na vez

input:
    accion
output:
    no es un heterograma
input:
    centrifugado
output:
    es un heterograma
    input:
        casa23
    output:
        no es valida
"""
string=input('Escribe una palabra: ')
if string.isalpha():
    string=string.lower()
    temp=set(string)
    if len(temp)==len(string):
        print('Es un heterograma')
    else:
        print('No es un heterograma')
else:
    print('Palabra no valida')
