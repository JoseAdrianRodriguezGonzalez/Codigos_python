# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:29:03 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripción: Strings as lists
"""
#Un string e suna secuencia (cadena) de caracteres 
#Usa la tabla decodificación definida por los caracteres.
#Una tabla de codificación es una tabla de traducción entre numeros binarios y caracteres.
# Estmaos usando la talba utf-8
#Strings son listas inmutables
#los caracteres en un indice especifico no pueden ser modificados
s='Hello world!'
print(s[0])
print(s[:5])#Slicing :chars from inde x0 to index 5-1)
print(s[5:])# slicing cars from index 5 to len(s-1)
print(s[:6:2])#slicing chars from index 0 to 6 in steps of 2
print(len(s))
#s[S]='s' #error
r='Hello'
t='world'
u=r+' '+t
w=r*3

##Comparing strings
a='Hello world!'
if a==s:
    print('yes')
s='Hello'
a='hello'
if a==s:
    print('Son iguales')
elif a>s:
    print('a es mayor que s')
else:
    print('a es menor que s')
###Iteration over string
# Ein string  hat der genau charakterik als ein list
for i in u:
    print(i)
for i in u[2:5]:
    print(i)
for i in u[::-1]:
    print(i)  #I iterats over the chars of u from end to begin)
#String sare inmutable,, so the methos always return a new string
#The methods do not modify the current string.
s1='                     hello world from Python world!\t\n'
s2='Alphabetic'
s3='1234'
print(s1.lower()) #Reutrns the lowcase version from s1
#i'll neew to save the result of the lower() method
print(s1.upper()) #Save the iuppercase versionn of s2
print(s1.strip())#retruns a string with whitespaces rmoed,
#from start and end
#whitespcae= spacetabas, return, newlines
#'',\t,\r,\n
print('asasasa\r deded')
print(s1.lstripe())#returns a string with withspaces remode, from start
print(s1.rstrip())#returns a string with withspaces remode, from end
print(s2.isalpha())#comprueba si todos los valores son alfabeticos 
print(s1.isdigit())#si todos los caracteres son numeros
print(s3.isdigit())
s4='1234.56'
print(s4.isdigit())
print(s1.isspace()) #tests if all charachters are whitspace
print(s1.isalnum())#test if all the characteres are alpha-numerics
print(s1.find())#searchs for the given string 'World witin s1 and return the first index wher it begins or -1 if is not found
print(s1.replace('world','jose')) #replaces all the ocurrences of the first string ('world')
#within the second string 'Everyone'
### String to list to string

s1="Hello world!how are you?"
words=s1.split("!")#returns a list of substring separated by the given delimiter. thE DELIMITER IS ANOTHER STRING. Whiout argument, the split are the whitespaces)
#the delimiter is ignored at the moment of the creation from the list, and doesn't belong to any sublist
words2=['Hola','Munda','que','tal']
word3=' '.join(words2) #returns a string created by concatenation from all string in a ista, separated by a delmiter -->''
