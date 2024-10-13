# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:25:43 2024

Descripcion: dado un string escribe un programa que genere otro string en donde
 todas las repeticiones del primer caracter
son reemplezadas por el caracterer '4'

s='Qué tal, cómo están . Qué han hecho'
output:
    $ué tal, cómo están . $ué han hecho
"""
s='Qué tal, cómo están. Qué han hecho'
lowers=s.lower()
caracter=s[0].lower()
remplazo=lowers.replace(caracter,'$')
        