# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 11:45:49 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción: Escribe un programa que cnalcule el área de un rectángulo con datos flotatnes dados por el usuario.
Al imprimir el ´rea, limita la precisión a 2 decimales
input:
    Dame la base: 6.7
    Dame la altura: 1.5
Ouput:
    El área del rectángulo es ...
"""
altura,base=float(input("Dame la altura: ")),float(input("Dame la base: "))
print(f' El área del rectángulo es  {(altura*base):.2f}')

