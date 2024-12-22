# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:45:09 2024

División: División de Ingenierías Campus Irapuato Salamanca
Carrera: Licenciatura en Ingeniería de Datos e Inteligencia Artificial
Curso: Fundamentos del Análisis de Datos
Semestre: Agosto-Diciembre 2024
Profesor: Juan Carlos Gómez Carranza
Autor: José Adrián Rodríguez González
Descripcion: basic pandas
"""
#Esuna paquete con funciones y modulos utiles para tabajar con datos estructurados
#tales como csv o json o xlsx
#csv=comma separated values

#Pandas, provee dost ipos de clases u objetos para manejar los datos

#Daots:
    #1.series; son objetos unidimensionales que están etiquetados, van a almacenar datoscomo enteros, string y objetos de python
    #1.Dataframes; un arreglo bidimenaional que almancena dato como s fuera un arreglo bidimensional o tabla con renglones y columnas.
import pandas as pd

####Series
#Para crear una serie neesitas el metodo s=pd.Series(data,index=index)
#los datos pueden ser varias cosas distintas 
#una lista
#un diccionario de python
#un arreglo dee numpy
#un valor escalar
#el indice e una lista de etiqueta para el eje

###Creatin  series from a list

s=pd.Series([1,3,5,15,6,8])
#Si el argumento indice no está definidio se indexa secuencialmente por numeros enteros empezando en 0

s=pd.Series([1,3,5,15,6,8],index=['a','b','c','d','e','f'])
#Ambas listas deben ser del mismo tamaño
#Vamos a crear una serie a partir de un diccionario 

d={'b':1,'a':0,'c':2}
s=pd.Series(d) #Se mantiene el orden creación
d={'a':0.0,'b':1.0,'c':2.0}
s=pd.Series(d,index=['b','c','d','a'])
#Changing the order for the indexes
#Al ser diferenete el tamaño de indices, por lo que los rellena con nan, el indice d no tiene un valor asociado por lo que pandas le asigna
#un valor nan

##from a saclar
s=pd.Series(5.0,index=['a','b','c','d','e','f'])
##Fills values for rows with the scalar

##Series as an array

s=pd.Series([1,3,5,15,6,8],index=['a','b','c','d','e','f'])
print(s[0],s['a'])
print(s[:3])#devuelve los valores de la posición 0 a la 3, retorna tambien los indicies
print(s[2::1])#slicing retorna los vlaore sde la posicion 2 hasta al final en pasos de dos
#primer valor de la serie

print(s[[2,1,5]])#ME devuelve los items en las posiciones indicadas

#Sereis como diccionario
print(s['c'])#esto me devuelve el valor asociado con el indice 'c' es 5
print('d' in s)#comprueba si el indice 'd' está en s
print('k' in s)#da flase

print(s['k']) #Marca error, ya que no existe el indice k
print(s.get('k'))#No marca error, pero me dice que este indice dice none
print(s.get('k','hola mundo'))
#eso me devuelve el valor el default si no existe



##vectorized operations
print(s+2)
#suma los elemento por elemento, es decir, le suma a cada elemento un 2
print(s-2)#resta a cada elemento 2
print(s*2)#le multiplica por dos
print(s/2)#/se divide
print(len(s))# me dice la longitud de s
print(sum(s))#suma todos los elementos de la serie
s1=pd.Series([2,4,7,5,1,9,10],index=['a','b','c','d','e','f','g'])
print(s+s1)
#Es tambien elemento por elemento, y los indice deben de coincidir, si no, se rellena con NaN



###Atributos
print(s.dtype)#imprime el tipo de dato de la serie,
print(s.hasnans)#dice si tienen nans
s2=s*s1
print(s2.hasnans)#Es un valor de nan

print(s.is_unique)#dice si todos los elementos de la serie son únicos
print(s.shape)#, dice el tamaño de la serie como una tupla
print(s.size)#size de una serie es un escalar
print(s.values)#Devueleve los valor de s en un arreglo

#metodos
print(s.abs())#obtiene el valor absoluto de la serie
print(s.argmax())#la posicion del maximo valor
print(s.argmin())#la posicion del minimo valor
print(s.argsort())#orden alas posiciones de valores de acuerdo alos valores
print(s.astype(str))#caste los valores a un tipode dato
s_c=s.copy()#hace una copia superifical, si tienee objetos complejos dentro de la serie, no se hace la copia profudna
#Cuando son objetos simples:
    #copy crea una copia dela serie, cuandoe l original es moficiado
    #la copia no es modificada
    
s3=s  #s_3 hace refeerenecia a la serie s, por lo que si se modifica algo del valor s. se modifica también en s3
s_c2=s.copy('deep') #esto hace una copia profunda, pero con objetos que son complejos
print(s.count()) #cuent todos los items que son no nulos o nans
print(s2.count())
print(s.cumsum())#la suma acumulativa
print(s.describe())#Esribe las estadísticas descriptivas de la serie

s.hist(bins=3)#graficar un histograma con los valores de la serie
print(s.min())#dice el minimo
print(s.max())# el maximo
print(s.mean())#promedio
print(s.mean())
print(s.mode())
print(s.std())
print(s.sum())

print(s.sort_values())#ordena los valroes de la serie
print(s.sort_index())#sort by index
print(s.value_counts())#cuenta el numero de vlaores unicos

lista=s.tolist()#caste los valores de una serei sino como una lista

####Dataframe
#Datafrae is a 2 dimensional labeled data structure. with columns of pottentially different types
###You can think of it like a spreadsheetor SQL table, or a dich of series object.
# It is generally the most commonly used pandas object.
##
# It has : data, index and columns 
#Data can be:
    #Dict of 1D arrar, lists dicts or Series
    #2-D numpy.ndarray
    #Structured or record ndarray
    #A Sereis
    #Another dataFrame 
#Index are row labels
#Colmnas are column labels

###Creating a data frame
##Froam a dict of lsists
d={'A':['a','b','c'],
   'B':['b','a','c'],
   'C':[1,2,3]}
df=pd.DataFrame(d)
#Dict keys are the columns names
#Indedxes are created sequentially (automatically)
#are not defined
df=pd.DataFrame(d,index=['ana','pedro','marta'])
####From a dict of dicts
d={'A':{'idx1':5,'idx2':6,'idx3':10},
   'B':{'idx1':5,'idx2':8,'idx3':20},
   'C':{'idx1':1,'idx2':2,'idx3':3}
}
df=pd.DataFrame(d)
#Outer dict keys are the columns names
#inner dict key are the indees

#From a list of dicts

lista=[{'a':1,'b':2},{'a':5,'b':10,'c':20}]
df=pd.DataFrame(lista)
#Not matching rows/columns are filled with NaN

##From a scalar
df=pd.DataFrame(0,columns=['Edad','Peso','Estatura'],index=['Juan','Pedro','Ana'])
#All cells are filed with the scalar
##Froma a dict of Series
d={'one':pd.Series([1,2,3],index=['a','b','c']),
   'two':pd.Series([10.0,15.0,25.0,40.0],index=['a','b','c','d'])}

df=pd.DataFrame(d)

#Not matchin rows/columns are filled with NaN


###Accsing data from DataFrame
d={'A':['a','b','c'],
   'B':['b','a','c'],
   'C':[1,2,3]}
df=pd.DataFrame(d,index=['row1','row2','row3'])
##Returns column A with indexes ->Series
df['A']
df.loc['row1'] #Retorna el renglon con ro1 (con el nombre de las columnas) -->Series
df.loc['row3','A'] #Retorma un valor en el renglo 'row3' de la columna 'A' -->El dato Object

df.iloc[2] #Returns row at location 2(columns names are indexes) --> Series
df[:2]#Slicing reutrns a slice of DF (rows)-->DataFrame

df[[True,False,True]]##Returns the rows in True locations -- > Dataframe

##Arithmetic operations
#Arithmetic operations are element wise
d=[{'A':3.5,'B':4.5,'Total':8.0},
   {'A':5.5,'B':12.5,'Total':18.0},
   {'A':7.5,'B':10.5,'Total':15.0},
   {'A':16.5,'B':27.5,'Total':41.0}
   ]
df_2=pd.DataFrame(d,index=['row1','row2','row3','Total'])



print(df_2*5+2) #Los multiplica por 5 y les suma 2
print(df_2/4)##Divide 
#Si hay valores nan, se quedan iguales 


print(df_2/df_2.loc['Total'])
#Divide a cada elemento por cada fila del dfde la fila 'total


print(df_2.div(df_2['Total'],axis=0))
##This divides element wise each column of the df by the column 'total'

print((df_2+2)/(df_2.loc['Total']+3))
##Hay varias 
##1. Se le suma al reglon 'total' 3
##2. Se suma dos a todo el dataframe 
##Se divide cada fila del df por el resultado de la fila dl paso 2 
##El data frame no es modificado
#Cada operacion produce un nuevo objeto (DataFrame o Series )

##Datafrmae align by colu,n and row names element-wise
d={'A':{'row1':'f','row2':'t','row3':'y'},
   'B':{'row1':'p','row2':'w'},
   'C':{'row1':10,'row2':11,'row3':12}}
df_3=pd.DataFrame(d)
print(df+df_3)
#For str--Concatenation
#For numbers -->sum
##Non values reamin the same
print(df.T)##Transpone
print(df.columns)#Column names
print(df.dtypes)#DataType of each column
print(df.index) #Indexes of DF
print(df.shape)#Returns a tupl ewith the shape of DF(rows,columns)
print(df.size)#Returns the numbers of items in DF
print(df.values)#Returns values of DF as a numpy array


###Methods
print(df_2.abs())##Valor absoluto
df_4=df.copy()##Shallow copy of df
df_5=df.copy=('deep')##Deep copy of df

print(df_3.count(axis=0)) #me cuenta los valores que no sean nan en el eje que identificque
#El eje igual 0, idica que son las columna
#el eje igual 1, indica que son los renglones 
print(df_2.cumsum(axis=1)) ##Cumulative axis of 0
print(df_3.nunique(axis=0))

m=df.to_numpy()#cast to numpy array


###Adding a clu,n to an existing DataFrame
#with insret

d={'nombre':['Laura','Pedro','Juan','Ana'],
   'estatura':[1.6,1.73,1.85,1.58]}
df_6=pd.DataFrame(d)
df_6.insert(1,'edad',[23,21,24,21])


##With a list
#create the list of new columns values
ciudad=['Salamanca','Salamanca','Irapuato','Salamanca']
df_6['ciudad']=ciudad


##Adding a ow toan existing DataFrme 
new_row=['Cintia',22,1.60,'Valle de Santiago']
df_6.loc[len(df)]=new_row
#Nota:
    #loc[] me permite acceder un grupo de renglones y columnas por etiquetas, pede ser también por un valor boolean
    #o un arreglo o locación [int]
##Now using Pandas for reading data from a file (CSV)

##All files have always
#ruta
#nombre
#extensión 
f_path="C:/Users/USUARIO/Documents/Universidad/terer/fundamentos/code/data/"
f_name="info_students"
f_extension='.csv'
file=f_path+f_name+f_extension

df=pd.read_csv(file)
#Metodo especifio para leer csv's
#.read_csv(file), read file as CSV and creates a Datafrma
#Normally: the first row, contains the column names
#if not specified, indexes are created automatically






















