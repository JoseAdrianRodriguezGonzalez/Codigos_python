# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 10:13:21 2024
División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licencia en Ingeniería en Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto- Diciembre 2024
Porfesor: Juan Carlos Gómez Carranza
@author: Rodríguez González José Adrián
Descripción: This is my first program in Pythn, Initializa some varaibles and print some reuslts.
"""
print("hola")
"""
Tarea

Escribir en una hoja (a mano) un peqeuño resumen sobre python. ¿Qué es? ¿qué tipo de lenguaje es?
 Una breve reseña de su historia.
¿Que características tiene?

tabla de coidficacion traduccion de caracteres abstractos a bits

Python es un lengujae interpretado, utiliza un interprete (kernel) para ejecutar directamente 
las instrucciones
sin pasar por una fase de compilación (y ligado).
NO genera dicrectamente un ejecutable

Dentro del interprete, pueden ejecutarse instrucciones por separado (de una en una o por bloque)
Si hay un error en una linea, se detiene la ejecución sin ejecutar el resto.
Lo que edscribimos aqui es un script 
---> Secuencia de instrucciones en un lenguaje interpreado

"""
#Python utilzia tipado dinámico de variables .
#No se necesita declarar el tipo de la variles de usarla.
#Python infiere el tipo a prartir del valor asignado durante la ejecución.
#El valor (y por tanto el tipo ) de la variable puede cambiar durante la ejecución.
#Tipos de datos primtivos
# entero,flotante,string,boleano=785,758.34,'hola mundo',False

#Cuando se inicialzia una variable, esta se queda
#en la memoria del ernel, tal forma que la puedo utilziar mientras exista.
#Si ya no la necesito, se puede borrar

#Python no necesita el punto y coma para indicar el fin d euna instrucción.
#Se puede colaor pero no es necesario (ni recomendable)
#En general en Python se esquera que haya solo 1 instrucción
#por línea (compacto)Python es case sensitive
# Distingue entre mayúsculas y minúsculas
#Convención: nombrar las variables con minpusculas
##Usando snake case. --> promedio_calificacion

### Inicialización y salida a terminal
a=5 #inicia la variable
a=7.5 #Cambia el valor de la variable (tipo)
b=6
c=-8
d=e=f=g=19
#salida a terminal
print(a)#eniva una salida a terminal insert una salto de línea al final. 
print(a*b)
print(a,c,f,d)
print(f'{a}--> {b}--> {c}')
print(f'{a:.2f}')
### Basci arithmeti operators
#returns a numerical value (int,float,imaginary)
a=b+c #sum
a=b-c #substraction
a=b*c #production
a=b/c #division
a=b//c #integer division
a=b%c #module
a=b**c #power x,y
##
a+=b #a+b
a-=b #a-b
a*=b #a*b
a/=b # a/b
a//=b #a//b
a%b #a%b
a**=b #a**b

###Comparison operators
# -->Retruns a boolean vlau: True or False
a==b #equal
a>b #greater than
a<b #less than
a!=b #different 
a>=b #greater than or equal
a<=b #less than or equal

###logical operatos
#--> returns a boolean value: True /False
i=True
j=False
i and j
i or j
not i
#Los operadores lógicos sirven para unir varias operaciones de comparación, oe l resultadod e operaciones
#lógicas
(a==b)and (e>g)
(a<b) and (e==c)
(a==b) or (e<g)

#Basic strings

s='¡hola mundo!'
t='¡hola mundo!'
#es indstinto el us de apostrofe o de comillas para definir un string
print(s)
print(t)
###El size en el explorador de variables, indica la longitud en caracteres del string.
###También puede obtneer la lognitud del string con la función len()

###Casting cambios de tipo de variables
k=9.7#float
l=str(k)#cast from float to string 
m=int(l)#cast from str to int (error)
m=float(l) #cast from str to float
n=int(k) #cast from float to int
p=bool('True')#cast from str to bool
o=bool(0) #cast from int to bool
q=bool(1) #cast from int to bool
n=input("Enter a number: ")#recie el str
n=int(input('Enter an integer number')) #lo cambia a int
n=float(input('Enter a number: ')) #lo cambia a float
n=int(n) #lo cambia de float a int

###Input
#input solicita una entrada al usuario en la terminal.
#Recibe como parámetro un string que se deplsiega 
#en la terminal
# 3-->input siempre reciba la entrada como un string(str)
# Si necesita la entrada en otro tipo, tengo que hacer casting


### Sobre variables
#Toda variable tien 3 propiedades
var= 'hola'
#Nombre:var
#tipo =str
#valor:'Hola'

###Precedencia de los operadores 
##Precedence     operators             associativity
# 1                  ()                   left to right
# 2                  x[index]
#                      x[index:index]      left to right
#3                   **                   Right to left
#4                    ++x,--x              Right to left
#5                    *,/,//,%             left to right
#6                   +,-                      left to right
#7                    in,not in
#                     is,is not
#                    <,<=,>,>=
#                    !=,==                 left to right
#8                    not x               right to lef+t
#9                   and                right to left
#10                   or                 right to left
exp=10+20*30
print(exp)   
##Noa sobre los operadores
#los operadores unarios (´+,-, --> sirven para cmair de signo un valor)
#solo tienen un operand
#Los operdaores binarios neecesitando dos operandos
exp=0
#Precedence of or y and
name ='Alex'
age=15
if (name== 'Alex' or name=='john') and age>18:
    print('Hello')
else:
    print('Not possible')

#If an expression contains two or more operators
#With the same precedence then Operator associativity
#is used to determine.
#It can either be left to right or from right to left

#left-rigth associativty
print(100/10*10)
#is calculated as(100/10)*10
print(5-2+3)
#is calculted as (5-2)+3
print(2**3**2)
#is calculted as 2**(3**2)
expr=100+200/10-3*10**2
print(exp)

# Tipos de variable por uso de variables omunes en programacion
#Contadores:Sirve para contar personas o iteraciones 
#Acumulador: Sirve para acumular cosas y está asociada con el contador
#Bnader: Indica el estado o propiedad de un elemento
