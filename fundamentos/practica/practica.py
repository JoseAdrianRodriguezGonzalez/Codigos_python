# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 10:20:02 2024

Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: 2024 Agosto-Diciembre
Práctica individual
Fecha:02-12-2024
Profesor:Dr. Juan Carlos Gómez Carranza
Autor:Rodríguez González
Descripción:
Hacer un programa que lea un archivo csv y haga distitnas operaciones estadísticas y que genere informes
"""

import pandas as pd
#Se obtienen las calificaciones 
import matplotlib.pyplot as plt 
def ingreso_nuevo_alumno(calificaciones):
    flag=True
    while flag:
        flag=False
        print("Alta de estudiante:\nDame la información del estudiante nuevo")
        #Pide el nombre
        nombre=input("Nombre: ").title()
        #Pide el semestre
        semestre=input("Semestre: ")
        if '-' in semestre and  len(semestre)==7:
            elements=semestre.split("-")
            if elements[0].isdigit() and not(int(elements[0])>=2000 and int(elements[0])<=2100):
                print("No tiene los años correctos")
                flag=True
            else:
                print("No son digitos")
                flag=True
                continue
            if not(elements[1].upper()=='AD' or elements[1].upper()=='EJ'):
                print(f"No tiene el formato correcto el {elements[1].upper()}")
                flag=True
                continue
            elements[1]=elements[1].upper()
        else:
            print("No presenta el formato correcto")
            flag=True
            continue
        #Pide la materia
        materia=input("Materia: ").title()
        #Pide la calificacion
        calificacion=float(input("Calificación: "))
        if not(calificacion>=0 and calificacion<=10):
            print(f"Calificacion erronea {calificacion}")
            flag=True
            continue
        #Pregunta sobre los duplicados
        duplicado = calificaciones[
            (calificaciones['Nombre'] == nombre) & 
            (calificaciones['Semestre'] == semestre) & 
            (calificaciones['Materia'] == materia)
        ]
        if not(duplicado.empty):
            print("Hay duplicados")
            flag=True
            continue
        #Si todo fue correcto lo escribe en el csv
        if not(flag): 
            with open("calificaciones.csv",mode="a",encoding='utf-8') as writer:
                calificaciones=writer.writelines(f'\n{nombre}','{"-"4.join(elements)},{materia},{calificacion}')

def informe(calificaciones):
        aprobados=calificaciones.copy()
        aprobados['Estados'] = aprobados['Calificación'].apply(lambda x: 'Aprobado' if x >= 7 else 'Reprobado')
        aprobados.to_csv("Estado.csv",encoding="utf-8")
def submenu(calificaciones):
    opcion=0
    while opcion!=4:
        print("1.Por estudiante")
        print("2.Por semestre")
        print("3.Por materia y semestre")
        print("4.Regresar")
        opcion=int(input("Ingrese una opcion"))
        if opcion==1:
            print("1.Por estudiante")
            estudiante=calificaciones.groupby("Nombre")
            print("Se están haciendo los cálculos")
            estudiantes={'Nombre': pd.Series(estudiante['Calificación'].mean().index),
                         'Mediana':estudiante['Calificación'].median().values,
                         'Promedio':estudiante['Calificación'].mean().values,
                         'Desviación':estudiante['Calificación'].std().fillna(0).values}
            df_estudiantes=pd.DataFrame(estudiantes)
            df_estudiantes.to_csv("estudiantes.csv",encoding="utf-8",index=False)
            print("el archivo estudiantes.csv se genero exitosamente ")
        elif opcion==2:
            print("2.Por semestre")
            semestre=calificaciones.groupby("Semestre")
            print("Se están haciendo los cálculos")
            semestres={'Semestre': pd.Series(semestre['Calificación'].mean().index),
                         'Mediana':semestre['Calificación'].median().values,
                         'Promedio':semestre['Calificación'].mean().values,
                         'Desviación':semestre['Calificación'].std().fillna(0).values}
            df_semestres=pd.DataFrame(semestres)
            df_semestres.to_csv("semestres.csv",encoding="utf-8",index=False)
            print("el archivo semestres.csv se genero exitosamente ")
        elif opcion==3:
            print("3.Por materia y semestre")
            materia_semestre=calificaciones.groupby(["Materia","Semestre"])
            materia_semestres={'Materia-Semestre': [f"{materia}-{semestre}"
                                                      for materia, semestre in materia_semestre.groups.keys()],
                'Mediana':materia_semestre['Calificación'].median().values,
                'Promedio':materia_semestre['Calificación'].mean().values,
                'Desviación':materia_semestre['Calificación'].std().fillna(0).values
            }
            df_materia_semestre=pd.DataFrame(materia_semestres)
            df_materia_semestre.to_csv("materias.csv",encoding="ISO-8859-1",index=False)
            print("el archivo materias.csv se genero exitosamente ")
        elif opcion==4:
            print("4.Regresar")
        else:
            print("Opcion incorrecta")

def graficas(calificaciones):
    print("Generando gráficas")
    semestre=calificaciones.groupby("Semestre")
    semestre.boxplot(column="Calificación",figsize=(8,4),fontsize=8)
    df_materia_semestre = calificaciones.copy()
    df_materia_semestre['Materia-Semestre'] = df_materia_semestre['Materia'] + '-' + df_materia_semestre['Semestre']
    df_materia_semestre.boxplot(column='Calificación', by='Materia-Semestre', vert=False,figsize=(12,7),fontsize=8)
    plt.show()
    print("Lás gráficas se crearon exitosamente")
def menu(opcion,calificaciones):
    if opcion==1:
        ingreso_nuevo_alumno(calificaciones)
    elif opcion==2:
        print("Informa de aprobados y reprobados")
        informe(calificaciones)
    elif opcion==3:
        print("Resúmenes")
        submenu(calificaciones)
    elif opcion==4:
        print("Opción 4")
        graficas(calificaciones)
    elif opcion==5:
        print("Opción 5, Adiós")
    else:
        print("Opción no valida")
calificaciones=pd.read_csv("calificaciones.csv",encoding="utf-8")
opcion=0
while opcion!=5:
    print("1.-Alta de calificación")
    print("2.-Informe de aprobación")
    print("3.-Resúmenes")
    print("4.-Gráficas")
    print("5.-Salir")
    opcion=int(input("Escirba una opción: "))
    menu(opcion,calificaciones)


