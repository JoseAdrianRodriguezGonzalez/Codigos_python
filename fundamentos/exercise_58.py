# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 18:56:34 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Ródriguez González José Adrián
Descripción: Dado un string (defínelo tú en el código),
escribe un programa que devuelva la cantidad de cada vocal que contiene.

s = 'Hola mundo que tal'

output:
	'Hola mundo que tal'
    Tiene 2 a
    Tiene 1 e
    Tiene 0 i
    Tiene 2 o
    Tiene 2 u

"""

s = 'Hola mundo que tal'
conto=0
conti=0
conta=0
conte=0
contu=0
for i in s:
    if i=='o':
      conto+=1
    elif i=='a' :
        conta+=1
    elif i=='u': 
        contu+=1
    elif i=='e' :
        conte+=1
    elif i=='i':
        conti+=1
print(f'{s}')
print(f'Tiene {conta} a')
print(f'Tiene {conte} e')
print(f'Tiene {conti} i')
print(f'Tiene {conto} o')
print(f'Tiene {contu} u')

#####
s=s.lower()
v='aeiou'
for i in v:
    print(f'Tiene {s.count(i)} {i}')