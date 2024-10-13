# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:02:29 2024

exercise_93

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción: Dada una tupla de tuplas, donde cada tupla
interna contiene strings, escribe un programa que solicite
un string al usuario y determine si se encuentra en alguna
de las tuplas internas y el número de tupla que es. En
caso de que no esté en ninguna tupla interna, mandar
un mensaje de error.

tupla = (('hola', 'mundo'), ('que', 'tal'),
		('como', 'te', 'va'), ('aqui', 'todo', 'bien'))

input:
    'te'

output:
    'te' está en la tupla 3

    
input:
    'Java'

output:
    'Java' no está en ninguna tupla
    """

tupla = (('hola', 'mundo'), ('que', 'tal'),
		('como', 'te', 'va'), ('aqui', 'todo', 'bien'))
string=input("Ingrese un string. ")
c=0
flag=0
for i in tupla:
    c+=1
    if string in i:
        print(f'{string} está en la tupla {c}')
    else:
        flag+=1
if flag==len(tupla):
    print(f'{string} no está en ninguna tupla ')