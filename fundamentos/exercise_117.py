# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 20:40:59 2024

@author: USUARIO
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Escribe un programa que juegue a los dados con
el usuario. 
	1. Que pregunte al usuario si quiere jugar (s/n).
	Convertir la entrada a minúsculas.
	2. Si se da una entrada no válida, mandar un mensaje de error 'Entrada no válida'
	3. Si el usuario da 'n' que envíe un mensaje de despedida '¡Gracias por jugar!'
	4. Si el usuario da 's' que el programa genere
	un número entre 2 y 12 y desplegarlo como el número
	de la suerte del usuario.
	5. Que el programa genere dos números enteros aleatorios
	entre 1 y 6 (los dos dados) y calcule su suma.
	6. Si la suma es menor o igual que el número del
	usuario, el	usuario gana. Mandar un mensaje de
	felicitación.
	7. Si la suma es mayor que el número del
	usuario, el usuario pierde. Mandar un mensaje de
	consolación.

input:
	¿Quieres jugar (s/n)? s
output:	
    Tu número de la suerte es: 7
    Dado 1: 2
    Dado 2: 6
    Suma de los dados: 9
    ¡Lo siento, perdiste :(!

input:
	¿Quieres jugar (s/n)? s
output:	
    Tu número de la suerte es: 8
    Dado 1: 1
    Dado 2: 3
    Suma de los dados: 4
    ¡Felicidades, ganate :)!
"""
import random as rn
opcion=input("Quieres jugar (s/n)?").lower()
if opcion=='s':
    numero_suerte=rn.randint(2,12)
    dado1=rn.randint(1,6)
    dado2=rn.randint(1,6)
    suma=dado1+dado2
    print(f'Tu numero de la suerte es {numero_suerte}')
    print(f'Dado 1:{dado1}')
    print(f'Dado 2:{dado2}')
    print(f"Suma: {suma}")
    if suma<=numero_suerte:
        print("Felicidades, ganaste")
    else:
        print("Lo siento, perditse Unu")
elif opcion=='n':
    print("¡Gracias por jugar!")
else:
    print("Entrada no valida")