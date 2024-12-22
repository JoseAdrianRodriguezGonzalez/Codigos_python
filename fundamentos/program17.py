# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 11:19:10 2024
Created on Tue Nov 12 10:52:30 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: Gómez Carranza Juan Carlos
Descripcion: General flies
"""

#A file is a contiguos set of byte suesd to persistently store data i a medya type (hard disk, ssd, magnetic tapes,...)
##These data are organizad in a specific forma an can be simple(text file or complex(exe program))
#The interla representation  of files are always bits
#FIles are mainly composed of three parts:
    #Header:etadadt about the contents of the file(file name, size, type, and so one)
    #data contents of the file as written by the creator or editor
    #end of file (EOF): Special character that indicates the end of the file
#Lo que representan estas partes y como están ordenadas depende de las especificaciones
# dle formato utilziado que generlaemnte esta difinido por la extension:
    # .jpg,
### File paths
#Cuando voy a acceder un archivo en un sistema operativo , como una dirección
#por lo general es un string que representa la ubicaión de un arcvhivo
#Esta copuesta por tres partes principale
#La ruta del folder: la ubicacion del folder del archvio en el sistema de archivos donde lso ubfolders,están serpadars por una /
#(Unix) o // en windows
#La segunda cosa encesaria es el nomrbe de archivo
#La ultima parte la extension, el fin de la ruta del archivo que está precedida por un punto
#Generalmente se utiliza para idnicar el tipo del archivo
    
f_path="C:/Users/USUARIO/Documents/Universidad/terer/fundamentos/code/data/"
#In python we need to use '/ in the path
#or to escape the '\' as '\\' and the path mut end with a '/
f_name='info_students'
f_extension='.csv'
f_file=f_path+f_name+f_extension
#Objeto que me permite manipular el archvio
reader=open(f_file)
#Reads the data --> returns a string with all the content in the file
data=reader.read()
reader.close() #close file
#Los tres pasos osn imortates: abrir, hacer algo, cerrar
#It is importnat to close the file to aoida unwnted behavior or leak of data
print(data)
      #With python there is a better option)
with open(f_file) as reader:
    
    data=reader.read()
    #The with statment automatically close the file once the block is finished
#Options are:
    # 'r': open for reading 
    # 'w':open for writting, truncating the file first(delete it first)
    #'x':open for exclusive creating, falling if the file alreayd exists
    #'a': open for writting appending to the end of file if it exists
    #'b':binary mode
    #'t':text mode
    #'+': open for updating reading and writins
    #the default mode if 'r' (open for reading text a synynm of 'rt')
    #mods of 'w+' and 'w+b' open and truncate the file

# rt, wt, xt, at
#rb,wb,xb,ab
#En text, utilizamods la tabla de codficaicon para interpretar los bytes

#rb,wt,xt,at
#rb,wb,xb,ab
##Types of files
#Text files
#Binary files (buffered or row)
#Files open is binary mode (using 'b' in the mode)
#returns contents as byte objects without any decoding.
#In text mode (the default or using 't'), the file content is returned as str,
#The bytes having ben first decoded using an encoding table
with open(f_file, 'rt') as reader:
    data=reader.read
with open(f_file,'rb') as reader:#Open fileas binary for reading
    data=reader.read()# Do something
#Data is type bytes
####Encodings 
#When creating a data text file, we MUST use a specific encoding.
#An encoding is a translation from byte to human readable
#Characters. This is typically done  by assigning a numerical value
#to represent a character.
#Common enoding are ASCII and UNCIDO (UTF-8,UT-16
#Parsing a text file with the incorrect encoding which it wasd created
#can lead failures or misrepresentations of the chars).
with open(f_file,'r',encoding='utf-8') as reader:
    data=reader.read()
with open(f_file,'r',encoding='iso8859-15') as reader:
    data=reader.read()
#Algunos caracteres están en posiciones diferentes en la talba
#de codficación, con respecto a la que se usó para crear el archivo   
with open(f_file,'r',encoding='ascii') as reader:
    data=reader.read()
    
#Hay caracteres que están fuera de la talba de codificación
#

#Nota:
#1.- If encoding is not specified, the encoding used is plataform dependent"


#2.- For binary files, leave encoding unespecified 
#Para saber la codificación de la plataforma
import locale
locale.getpreferredencoding()
#Devuelve la codifiación por default de la plataforma
#cp65001


####Line ending
#When working with (text) data file , it is necessary to indicate 
#Two standards:
    #American National Standards Institue (ANSI)
        #- Carriage return (CR \r)
        #An the Line Feed(LF or ,\n) characters
        #-->(CR+LR or \r\n)
    #organization for standarization (ISO)
    #either the CR+LF of 
    #just the LF characters (\r\n or \n )
    
#Operating systems
#Windows uses the CR+LF characters (\r\n)
#unix/linux (ios) use the LF character(\n)
#Howvever, we need to account for different situations
#File objects
#Whene opening a file, it creates a file object.
#That is an object exposing a file oriented API
#wITH METHODS SUCH AS READ() or write()) to an underlyinh resourve (real on disk file, or anther)
#or another type of storage or computational device).
####Reading methods
    
with open(f_file,'r',encoding='utf-8') as reader:
    data=reader.read(5)
###Writing method
    