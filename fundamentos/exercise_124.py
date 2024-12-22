# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:08:40 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Escribe una función que reciba un string y que
devuelva el número de vocales y consonantes que contiene.

def contar_letras_2(frase):
	pass

contar_letras_2('Hola MUndo!')
output:
    vocales: 4
    consonantes: 5
"""
def contar_letras_2(frase):
    vocal='AEIOUaeiou'
    cvocal=0
    cconsonante=0
    for i in frase:
        if i in vocal :
            cvocal+=1
        elif i.isalpha():
            cconsonante+=1
    return cvocal,cconsonante
vocal,consonante=contar_letras_2('Hola MUndo!')
print(f'vocales: {vocal}\nconsontante: {consonante}')

