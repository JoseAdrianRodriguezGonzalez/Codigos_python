# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:48:10 2024

@author: USUARIO
"""
camposdados = ['nua', 'nombre', 'carrera', 'semestre']
estudiantes = [ ['1', 'Camacho Hernández Daniela', 'LIDIA', 1],
               ['2', 'Cervantes Martínez Rodrigo', 'LIDIA', 2], 
               ['3', 'Frías Cortez Rafael Alejandro', 'LIDIA', 3], 
               ['4', 'González Mendoza Valeria Dalay', 'LIDIA', 4],
               ['5', 'Liedo Castellanos Esteban', 'LIDIA', 5], 
               ['6', 'Ramírez Gutiérrez Camila', 'LISC', 1],
               ['7', 'Ramos Soto Omar', 'LISC', 2],
               ['8', 'Sánchez Vallejo Eduardo', 'LISC', 3],
               ['9', 'Castro Lucero Perla Estefania', 'LISC', 4],
               ['10', 'Chavez Islas Jair', 'LISC', 5]]
entrada=''
while entrada!='salir':
    entrada=input("Dame una instruccion")
    entrada=entrada.lower()
    entrada=entrada.replace(' ','')
    ##validar si es una entrada salir
    if entrada== 'salir':
        break
    partes=entrada.split('|')
    instruccion=partes[0]
    #### validar si es select o si es delete
    if instruccion=='select' :
        if len(partes)!=3:
            print('Instruccion no reconocida')
            continue
            #obtener los campos
        campos=partes[1].split(',')
        if len(campos)>4:
            print("Demasiados campos")
            continue
        error=0
        campo=''
        for campo in campos:
            if campo not in camposdados:
                error=1
                break
            if camposdados.count(campo)>1:
                error=2
                break
        
        if error==1:
            print(f'{campo} no existe')
            continue
        elif error==2:
            print(f'{campo} no existe')
            continue
        condicion=partes[2]
        partes_cond=[]
        operador=''
        if '=' in condicion :
            partes_cond=condicion.split('=')
            operador='='
        elif '>' in condicion :
            partes_cond=condicion.split('>')
            operador='>'
        elif'<' in condicion :
            partes_cond=condicion.split('<')
            operador='<'
        elif '&' in condicion :
            partes_cond=condicion.split('&')
            operador='&'
        print(partes_cond)
        if len(partes_cond)!=2:
            print('la condicion no es valida')
            continue
        campo_cond=partes_cond[0]
        if (operador== '&' and campo_cond=='semestre'):
            print('El operador no es válido')
            continue
        if campo_cond not in campos:
            print('El campo en la condición no existe')
        valor_comp=partes_cond[1]
        if campo_cond=='semestre':
            valor_comp=int(valor_comp)
        idx_camp=[]
        for campo in camposdados:
            idx_camp.append(campos.index(campo))
        idx_camp_cond=campos.index(campo_cond)
        print(idx_camp_cond)
        #seleeccionar estudiantes
        seleccionados=[]
        for estudiante in estudiantes:
            valor_est=estudiante[idx_camp_cond]
            if campo_cond !='semestre':
                valor_est=valor_est.lower()
                estudiante_campos=[]
                if operador =='=':
                    if valor_est==valor_comp:
                        for idx in idx_camp:
                            estudiante_campos.append(str(estudiante[idx]))
                if operador =='>':
                    if valor_est>valor_comp:
                        for idx in idx_camp:
                            estudiante_campos.append(str(estudiante[idx]))
                if operador =='<':
                    if valor_est<valor_comp:
                        for idx in idx_camp:
                            estudiante_campos.append(str(estudiante[idx]))
                if operador =='&':
                    if valor_est in valor_comp:
                        for idx in idx_camp:
                            estudiante_campos.append(str(estudiante[idx]))
                if len(estudiante_campos)>0:
                    registro=','.join(estudiante_campos)
            for estudiante in seleccionados:
                print(estudiante)
    elif instruccion=='delete':
        if len(partes)!=2:
            print('Instruccion no reconocida')
            continue
        campos=partes[1].split(',')
        if len(campos)>4:
            print("Demasiados campos")
            continue
        error=0
        campo=''
        for campo in campos:
            if campo not in camposdados:
                error=1
                break
            if camposdados.count(campo)>1:
                error=2
                break
        
        if error==1:
            print(f'{campo} no existe')
            continue
        elif error==2:
            print(f'{campo} no existe')
            continue
        condicion=partes[2]
        partes_cond=[]
        operador=''
        if '=' in condicion :
            partes_cond=condicion.split('=')
            operador='='
        elif '>' in condicion :
            partes_cond=condicion.split('>')
            operador='>'
        elif'<' in condicion :
            partes_cond=condicion.split('<')
            operador='<'
        elif '&' in condicion :
            partes_cond=condicion.split('&')
            operador='&'
        print(partes_cond)
        if len(partes_cond)!=2:
            print('la condicion no es valida')
            continue
        campo_cond=partes_cond[0]
        if (operador== '&' and campo_cond=='semestre'):
            print('El operador no es válido')
            continue
        if campo_cond not in campos:
            print('El campo en la condición no existe')
        valor_comp=partes_cond[1]
        if campo_cond=='semestre':
            valor_comp=int(valor_comp)
        idx_camp=[]
        for campo in camposdados:
            idx_camp.append(campos.index(campo))
        idx_camp_cond=campos.index(campo_cond)
        print(idx_camp_cond)
        #seleeccionar estudiantes
        seleccionados=[]
        for estudiante in estudiantes:
            valor_est=estudiante[idx_camp_cond]
            if campo_cond !='semestre':
                valor_est=valor_est.lower()
                restantes=[]
                if operador =='=':
                    if valor_est==valor_comp:
                        for idx in idx_camp:
                            restantes.append(str(estudiante[idx]))
                if operador =='>':
                    if valor_est>valor_comp:
                        for idx in idx_camp:
                            restantes.append(str(estudiante[idx]))
                if operador =='<':
                    if valor_est<valor_comp:
                        for idx in idx_camp:
                            restantes.append(str(estudiante[idx]))
                if operador =='&':
                    if valor_est in valor_comp:
                        for idx in idx_camp:
                            restantes.append(str(estudiante[idx]))
                estudiante=restantes
    else:
        print("Instruccion no reconocida")