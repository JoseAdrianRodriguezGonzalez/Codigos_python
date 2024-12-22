# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 11:31:41 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripición: Random numbers
"""

import random as rn
#random es el modulo para numeros aleatorios
#le cambia el nombre a rn
print(rn.random())# returns the  next random floating point number
#in the range [0.0,1.0) <- se excluey
rn.uniform(100,200)#Retrusn a random
#floating point number
#between [100,200] with a unifrom distribution
# Notas:
    #El modulo random genera secuencias de numeros
    #pseudoaleatorios
    #No son realemnte números aleatorios
    #La computadora funciona de manera determinsita
    #misma entrada->misma salida
    #los numeros pseudoaleaorios simmulan una aleatoriedad a traves
    #de ecuaciones
    #Estas ecuaciones se basan en estados cambiantes del sistmea
    #--> hora del sistema(nivel de ms)
    #la ecuacion de los numeros aleatoiors
    #toma como base una semilla
    #la semilla se puede dar directamente, ose toma del estado
    #cabiante del sistema(computadora) --> hora del sistema
    #la seuencia de numeros aleatorios se inicia con la semilla
    #y a partir de ella se generan los siguientes.
    #Si la semilla se vuelve a iniciar, la secuencia será la misma
    #definir la semilla inicial de ls numeros pseudoaleatorios+
    #Este es un problema ya que se pueden volver a generar las mismas secuencias de valroes
    #Random no es una libería que debería utilizar para7
    #cuestiones de seguridad (criptografía)
rn.seed(1)
print(rn.random())
#si reiniciamos la semilla, su secuencia se reinicia
#Para evitar que la secuencia se repetitiva, se utiliza
#un numero qye se suele tomar de un estado cambiante
#del sistema
#--> hora del sistema
#si el generador toma la semilla del sistema en una hora en particualr
#al dia siguiente, al ejecutar el programa, puede coincidir que sea la misma semilla.
rn.randint(100, 200) #retrurns a random integer n such that
# a<=n<=b
#a=100,b=200
x=['a','b','c','d','e','f','g','a','b','c']
rn.choice(x) #me regresa un objeto aleatorio de una lista(iterable)
s='hols mundo uwu'
rn.choice(s)
#caracter de escape \n, para poner doble diagnoal \\
string_1=r'hola\t mundo'#toma literal el string
rn.choices(x,k=3)#, me devuleve k iterables puede tomar dos o más veces el
# mismo elemento
rn.sample(x,3)#regresa una lsita con k (3) elementos unicos
#seleccionados desde la lista, sin reemplazo
#No puedo seleccionar el mismo objeto
#La propiedad unica no es sobre el valor del item,(esto quiere decir, que puedo seleccionar dos c)
#Tiene que ver con la posición de los objetos.
rn.shuffle(x)#revuelve la lista (debe ser una lista)
#lo va a hacer en la lista,(inplace) 