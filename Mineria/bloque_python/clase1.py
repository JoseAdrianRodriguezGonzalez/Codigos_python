#COECCION ORENADAS DE ELEMENTOS MUTABLES
#eSTA INDEXADOS ES DECIR SE PUEDE ACCEDER A SUS SELEMENTOS MEDIANTE INDICIES

#lOS ELEMENTOS PUEDEN SER DE DIFERENTES TIPOS.
#oBJETO ITERALE

lista= [1,2,3,4,5,6]
lista_2=[1,'a','b',[1,2],('s','a')]

#print(lista[:])

#FUnciones

#Tamañ de la lista


size=len(lista)

#Extend añade mas de 1 elemento

nueva=lista.extend(lista_2)

#la funcion pop es util cuando se quire deir que elemento es el que se desea eliminar

lista.pop()

#index, la funcion te encuentra la primera ocasion en donde esta un elemento
lista.index(3)

#lista concatenacion
lista_3=lista+lista_2

#Repeticion de iterables
lista5=lista_3*3

val ='hola'

#COntar apariciones

lista5=lista.count(1)
#Ordenar
lista_6=[(2,1),(1,7)]
print(lista_6.sort())

#Referencias
a=[[1],[2],[3],[4],[5],[6],[7]]
b=a
b[0][0]=8
print(a)
print(b)



#Strings

s='a'

student_type=[
    ('john','A',15),
    ('jane','B',12),
    ('dave','B',10),
 ]
student_type.sort()
print(student_type)


l_int=[1,2,3,4,5]
print("-".join(str(ele) for ele in l_int))


print("hola    ".strip())
str_2="hola mundo".split()
#isalpha
      #isnumeric
#replace(old,new,count)
#isdigit
#isalnum
#isspace
#isdigit
print("hola mundo".find("mu"))
