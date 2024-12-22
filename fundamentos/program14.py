# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:24:26 2024


División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Basci use of modules

"""

#A module is a file containing Python definitions functions
#and statemnts.The file name is the module name with suffic
#py appended within a module, the module's name(as a string)
#is available as the value of the global variable __name__
#import operaciones
import operaciones 
#debemos estar ubicados en el directorio dende s enecuentra el modulo que queremos importar
#Cambiar el directorio de trabajo en la parte superior
#Other alternative is create a directory a la varible de entorno PATH
#Se importan las definiciones localizadas en matematicas.py
#No se improtan de maner aindividual, se importa todo el modulo
lista=[5.0,6.7,7.8,8.3,9.3,1,2,3]
#Para acceder a las fucioens definidicas en matameticas.py
#Tengo que hacer refrenecia a ellas utilizando la notacion
print(operaciones.suma(lista))
print(operaciones.promedio(lista))
print(operaciones.minimo(lista))
print(operaciones.maximo(lista))
#Podemos cambiar el nobre del modulo
import operaciones as op
print(op.suma(lista))
print(op.promedio(lista))
print(op.minimo(lista))
print(op.maximo(lista))
print(op.__name__)#Imprimer el nombre del modulo
#Importing only one definition from a modlule
from operaciones import suma
print(suma(lista))
#Importa solo la definicion de la funcion suma
#Cambiar el nombre de la definicion importada
from operaciones import promedio as pm
print(pm(lista))
#ecesito varias definiciones
from operaciones import suma,promedio
print(suma(lista))
print(promedio(lista))
##Se pueden camiar el nombre así

from operaciones import suma as sm,promedio as pm
print(sm(lista))
print(pm(lista))
#Importar todas las definciones que form el modulo
from operaciones import  *
##importa cada defincion de forma individual 
#ya nose necesario usar la notacion
print(minimo(lista))
print(operaciones.__doc__)