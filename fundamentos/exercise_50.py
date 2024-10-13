# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:02:16 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Ródriguez González José Adrián
Descripción: Escribe un programa que solicite strings
(palabras) al usuario de forma continua hasta que ingrese
la palabra 'Fin'. Que las palabras las vaya guardando en
una lista de listas. Cada lista interna se debe llenar con
solo 3 palabras. Cuando la palabra ya se encuentre en la
lista interna, que el programa no la agregue y escriba en
la terminal '¡Palabra repetida!', y continua pidiendo más
palabras. La palabra 'Fin' ya no se guarda en ninguna
lista.

lista = [[]]

input:
	Dame una palabra: hola
lista = [['hola']]

input:
	Dame una palabra: mundo
lista = [['hola', 'mundo']]

input:
	Dame una palabra: que
lista = [['hola', 'mundo', 'que']]

input:
	Dame una palabra: tal
lista = [['hola', 'mundo', 'que'], ['tal']]

input:
	Dame una palabra: tal
output: '¡Palabra repetida!'

input:
	Dame una palabra: que
lista = [['hola', 'mundo', 'que'], ['tal', 'que']]

input:
	Dame una palabra: Fin

output:
	[['hola', 'mundo', 'que'], ['tal', 'que']]

"""
lista=[[]]
palabra=''
i=0
j=0
while palabra!='Fin':
    palabra=input('Dame una palabra')
    if palabra in lista[i]:
        print('Palabra repetida')
        continue
    if palabra=='Fin':
        break
    if j<3:
        lista[i].append(palabra)
        j+=1
    else:
        j=0        
        lista.append([])
        i+=1
        lista[i].append(palabra)