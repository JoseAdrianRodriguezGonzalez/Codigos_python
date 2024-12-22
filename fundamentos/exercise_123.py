# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 22:37:25 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Escribe una función que reciba un string y que
devuelva el número de letras mayúsculas y minúsculas que
contiene.

def contar_letras(frase):
	pass

contar_letras('Hola Mundo!')

output:
    mayúsculas: 2
    minúsculas: 7
	
"""
def contar_letra(string):
    mayu=0
    minu=0
    for i in string:
        if i.islower():
            minu+=1
        elif i.isupper():
            mayu+=1
    return minu,mayu
minu,mayu=contar_letra('Hola Mundo!')
print(f'mayúsculas: {mayu}\n minusculas: {minu}')