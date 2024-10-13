# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:40:55 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción: En un restaurante el  costo  de  platillo  por
persona  es  de  $95.00, pero si van en grupo es más 
barato. Si es un grupo de más de 20 pero menor o igual a 
30 personas el costo baja a $85.00. Para más de 30
personas el costo baja a $75.00. Escribe un programa que 
calcule el total de la cuenta a pagar para un grupo de X
personas (dado por el usuario). Limita la precisión a 2 
decimales.
    
input:
    Dame el total de personas: 25
output:
    El total de la cuenta es: $2125.00

input:	
	Dame el total de horas: 50
output:
    El total a pagar es: $3750.00
"""

personas=int(input('Dame el total de personas: '))
costo=95.00
if (personas>20) and (personas<=30):
    costo=85.00
elif (personas>30):
    costo=75.00
print(f'El total de la cuenta es: {personas*costo}')