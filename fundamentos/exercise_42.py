# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:14:44 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Descripción: Dada una lista de strings (creada por ti
directamente en el código) y un número n (entero positivo)
solicitado al usuario, escribe un programa que divida la
lista original en sublistas de tamaño n. Solo la última
lista puede contener menos de n elementos. Que el programa
genere una nueva lista con estas sublistas.

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
input:
	Dame un número (entero positivo): 3

output:
    [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j']]

"""

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
n=int(input("Dame un número entero positivo: "))
count=0
listan=[]
lista_salida=[]
for i in lista:
    listan.append(i)
    if len(listan)==n:
        lista_salida.append(listan)
        listan=[]
        count+=1
    elif count==len(lista)//n:
        continue
if len(listan)>0:
    lista_salida.append(listan)
print(lista_salida)