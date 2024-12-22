# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 20:52:29 2024


@author: USUARIO
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Escribe un programa que:
	1. Genere un número aleatorio entre 1 y 100.
	2. El programa debe preguntar por el número al usuario
	"Adivina el número que pensé: "
	3. Si el número dado por el usuario es menor o mayor,
	escribir en la terminal "El número que tengo es <menor>
	o <mayor>".
	4. Se debe repetir el paso 2 y 3, hasta que el usuario
	logre adivinar el número.
	5. Cuando logre adivinarlo, mandar un mensaje de
	felicitación y el número de intentos que hizo.

numero = 57
input:
	Adivina el número que pensé: 50
output:
	El número que tengo es mayor
input:
	Adivina el número que pensé: 60
output:
	El número que tengo es menor
input:
	Adivina el número que pensé: 55
output:
	El número que tengo es mayor
input:
	Adivina el número que pensé: 57
output:
	¡Felicidades lo has adivinado!
	Hiciste 4 intentos
"""

import random as rn 
numero=rn.randint(1,100)
adivinar=0
count=0
while adivinar!=numero:
    adivinar=int(input('Adivina el número que pensé: '))
    if adivinar>numero:
        print("El numero que tengo es menor")
        count+=1
    elif adivinar<numero:
        print("El numero que tengo es mayor")
        count+=1
    else:
        print("¡Felicidades  lo has adivinado")
        count+=1
        print(f"Hiciste {count} intentos")
        break
