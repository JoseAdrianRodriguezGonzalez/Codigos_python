# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:13:57 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Escribe una función que reciba un string, que lo
separe por espacios y devuelva un diccionario en donde la
llave es cada substring y el valor es el número de veces que
ese substring aparece en el string principal.

def contar_palabras(frase)
	li = ['hola', 'todo', 'bien', 'aqui', 'hola', 'aqui',
		'estamos', 'bien']
	pass
	
s = 'hola todo bien aqui hola aqui estamos bien'
contar_palabras(s)

output:
	d = {'hola':2, 'todo':1, 'bien':2, 'aqui':2, 'estamos':1}
"""
def contar_palabras(frase):
    li=frase.split(' ')
    set1=set(li)
    d={}
    for i in set1:
        d[i]=li.count(i)
    return d
s = 'hola todo bien aqui hola aqui estamos bien'
print(contar_palabras(s))
