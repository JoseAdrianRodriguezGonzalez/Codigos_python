# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:08:29 2024
Created on Tue Nov 12 10:52:30 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripcion: Dada una lsita de tuplas, cada tupla con 3 numeros flotantes, esribe un programa usando funciones lamda que la
ordene de fora ascendente pr le valor absoluto del segundo elemento
lista=[(-1.5,-1.6,-2.6),(8.9,1.2,2.4),(9.1,-3.5,4.5),(0.4,-9.0,3.5)]
output:
lista=[(8.9, 1.2, 2.4), (-1.5, -1.6, -2.6), (9.1, -3.5, 4.5), (0.4, -9.0, 3.5)]
"""
lista=[(-1.5,-1.6,-2.6),(8.9,1.2,2.4),(9.1,-3.5,4.5),(0.4,-9.0,3.5)]
lista.sort(key=lambda x:-x[1])
print(lista)