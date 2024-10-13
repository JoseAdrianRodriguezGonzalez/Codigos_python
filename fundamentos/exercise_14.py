# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:50:58 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Decripcion: Escribe un programa que determine la cantidad
del bono navideño que recibrá un empleado solicitando su
antigüedad en años y su salario semanal (salario por 7
días). Considera que si su antigüedad es mayor a cuatro
años o su sueldo semanal es menor de 2000 pesos, le
corresponde un 25% de su sueldo mensual (salario de 30
días), en caso contrario le corresponde un 20% del sueldo
mensual. Limita la precisión a 2 decimales.
    
input:
    Dame la antigüedad del empleado (años): 5
    Dame su sueldo semanal: 1500

output:
    Su bono navideño es: $375.00
"""
anios=int(input('Dame la antiguedad del empleado (años): '))
sueldo=float(input('Dame su sueldo semanal: '))
sueldo=(sueldo/7)*30
bono=0
if(anios>4) or (sueldo<2000):
    bono=0.25
else:
    bono:0.20
print(f'Su bono navideño es:$ {(bono*sueldo):.2f}')