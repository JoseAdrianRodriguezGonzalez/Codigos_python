# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:53:55 2024
Carrera:Licenciatura en Ingeniería de Datos e Inteligencia ARTIFICIAL
cURSO: Fundamentos del Análisis de Datos
Semestre: 2024 Agosto-Diciembre
Examen práctico 1
Fecha: 24-09-2024
Profesor: Dr. Juan Carlos Gómez Carranza
Autor: Rodríguez González José Adrián
Descripción:
    
    base de datos
    
"""

####3 ejercicios
campos=['nua','nombre','carrera','semestre']
estudiantes=[
    ['1', 'Camacho Hernández Daniela', 'LIDIA', 1],
    ['2', 'Cervantes Martínez Rodrigo', 'LIDIA', 2],
    ['3', 'Frías Cortez Rafael Alejandro', 'LIDIA', 3],
    ['4', 'González Mendoza Valeria Dalay', 'LIDIA', 4], 
    ['5', 'Liedo Castellanos Esteban', 'LIDIA', 5],
    ['6', 'Ramírez Gutiérrez Camila', 'LISC', 1],
    ['7', 'Ramos Soto Omar', 'LISC', 2],
    ['8', 'Sánchez Vallejo Eduardo', 'LISC', 3],
    ['9', 'Castro Lucero Perla Estefania', 'LISC', 4],
    ['10', 'Chavez Islas Jair', 'LISC', 5]]
peticion=''
queries=[]
request=[]
value=[]
response=[]
request_index=[]

while(peticion!='salir'):
    queries=[]
    request=[]
    value=[]
    response=[]
    request_index=[]

    peticion=input('')
    peticion=peticion.lower()
    peticion=peticion.replace(' ','')
    instruc=['select','delete','salir']
    if (instruc[0] in peticion) or (instruc[1] in peticion) or(instruc[2] in peticion):
        if (peticion.count('|')>2):
            print('Peticion no valida')
        else:
            queries=peticion.split('|')
            request=queries[1].split(',')
            compar=''
            if '=' in queries[2]:
                value=queries[2].split('=')
                compar='='
            elif '>' in queries[2]:
                value=queries[2].split('>')
                compar='>'
            elif '<' in queries[2]:
                 value=queries[2].split('<')
                 compar='<'
            elif '&' in queries[2]:
                 value=queries[2].split('&')
                 compar='&'
                
            query=queries[0]
            
            repe=False
            for k in request:
                if k in campos:
                    request_index.append(campos.index(k))
                elif request.count(k)>1:
                    print('datos repetidos')
                    repe=True
                    break
                else:
                    print(f'El campo {k} no existe!')
            if len(request)>4:
                print('¡Demasiados campos ingresados!')
            if queries[0]=='select':
            
                entero=0
                variable=''
                busqueda=campos.index(value[0])
                if value[0]=='semestre':
                    entero=int(value[1])
                    if compar=='=':
                        resultados=[]
                        for i in estudiantes:
                            if repe==True:
                                break
                            if entero == i[busqueda]:
                                for j in request_index:
                                    resultados.append(i[j])
                        print(resultados)
                    elif compar=='>':
                        resultados=[]
                        for i in estudiantes:
                            if repe==True:
                                break
                            if entero < i[busqueda]:
                               for j in request_index:
                                   resultados.append(i[j])
                        print(resultados)
                    elif compar=='<':
                        resultados=[]
                        for i in estudiantes:
                            if repe==True:
                                break
                            if entero > i[busqueda]:
                                for j in request_index:
                                    resultados.append(i[j])
                            
                        print(resultados)
                else:
                    variable=value[1]

                    if compar=='=':
                        resultados=[]
                        for i in estudiantes:
                            if repe==True:
                                break
                            if variable==i[busqueda].lower():
                                for j in request_index:
                                    resultados.append(i[j])
                        print(resultados)
                    elif compar=='>':
                        resultados=[]
                        for i in estudiantes:
                            if repe==True:
                                break
                            if variable<i[busqueda].lower():
                               for j in request_index:
                                   resultados.append(i[j])
                        print(resultados)
                    elif compar=='<':
                        resultados=[]
                        for i in estudiantes:
                            if repe==True:
                                break
                            if variable>i[busqueda].lower():
                                for j in request_index:
                                    resultados.append(i[j])
                                
                    repe=False
            elif query=='delete':
                entero=0
                variable=''
                busqueda=campos.index(value[0])
                entero=int(value[1])
                if compar=='=':
                    resultados=[]
                    for i in estudiantes:
                        if repe==True:
                            break
                        if entero == i[busqueda]:
                            estudiantes.remove(i)
                    print(estudiantes)
                elif compar=='>':
                    resultados=[]
                    for i in estudiantes:
                        if repe==True:
                            break
                        if entero < i[busqueda]:
                            estudiantes.remove(i)
                    print(estudiantes)
                elif compar=='<':
                    resultados=[]
                    for i in estudiantes:
                        if repe==True:
                            break
                        if entero > i[busqueda]:
                            estudiantes.remove(i)
                    print(estudiantes)
            else:
                variable=value[1]
                for i in estudiantes:
                    if repe==True:
                        break
                    if variable==i[busqueda].lower():
                        estudiantes.remove(i)
                print(estudiantes)
                repe=False
                    
                    
    else:
        print('Peticion no valida')