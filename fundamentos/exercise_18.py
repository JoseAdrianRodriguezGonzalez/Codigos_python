# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:20:40 2024


Created on Tue Aug 27 10:56:59 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripcion :Escribe un programa para determinar cuánto ahorrará una persona en 1
 año si cada mes
deposita una cantidad flotante dada de dinero(pedirla al usuario,cada mes puede
                                              depositar una cantidad 
                                              diferente).

"""
sume=0
for i in range(12):
    depos=float(input(f"Cuanto depositaste en el mes {i+1}:"))
    sume+=depos
print(f'El total ahorrado es: {sume:.2f}')

