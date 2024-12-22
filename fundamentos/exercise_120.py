# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:18:01 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripcion:Escribe una funcion que reia una lsitra d enimeros entero y que devuelva Yrue si la lsita está ordenada de forma ascendente
y False en caso contrario

"""
lista=[1,2,3,4]
lista2=[6,7,2,7,9]
def ordenada(lista):
    lista_2=[i for i in lista]
    lista_2.sort()
    if lista==lista_2:
        return True
    else:
        return False
print(ordenada(lista))
print(ordenada(lista2))