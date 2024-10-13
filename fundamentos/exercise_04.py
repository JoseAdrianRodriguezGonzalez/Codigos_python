# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 10:44:19 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción: Escribe un programa que determine el sueldo semanal de un 
trabajador, solicitando las horas trabajadas en la 
y el pahgo que se la hace por hora. Limita la precisión a 2 decimales.
input : 
    Dame el total de hora trabajadas: 45
    Dame el pago por hora: 80
output:
    el sueldo semanal es...
"""
total_horas=int(input('Dame las horas que trabajas = '))
pago_horas=float(input('Dime lo que te pagan por hora = '))
print(f"te van a dar = ${(total_horas*pago_horas):.2f}")
