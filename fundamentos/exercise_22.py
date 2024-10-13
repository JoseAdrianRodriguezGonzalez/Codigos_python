# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 01:40:01 2024

@author: USUARIODivisión: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción:  Escribe un programa que lea una cantidad n
de calificaciones flotantes (pide n al usuario)
correspondientes a un grupo de estudiantes y que
determine el nÃºmero de aprobados (>=6) y de
reprobados (<6). Valida que las calificaciones estánn
entre 0 y 10. Si no lo estÃ¡, envÃ­a un mensaje de error
y no la consideres en las cuentas.
    
input:
    Dame cuÃ¡ntos estudiantes son: 5
    
    Dame la calificaciÃ³n 1: 6.5
    Dame la calificaciÃ³n 2: 5.8
	Dame la calificaciÃ³n 3: 12
output:
	Â¡CalificaciÃ³n invÃ¡lida!
input:
    Dame la calificaciÃ³n 4: 9.5
	Dame la calificaciÃ³n 5: 8.5
output:
    El nÃºmero de estudiantes aprobados es 3
	El nÃºmero de estudiantes reprobados es 1
"""

alumnos=int(input('Dame cuántos estudiantes son: '))
aprobados=0
reprobados=0
for i in range(alumnos):
    calif=float(input('Dame la calificación: '))
    if calif<0 or calif>10:
        print("Calificación invalida")
        continue
    else:
        if calif>=6:
            aprobados+=1
        elif calif<6:
            reprobados+=1
        
print(f'La cantidad de personas aprobadas es: {aprobados}')
print(f'La cantidad de personas reprobadas es: {reprobados}')