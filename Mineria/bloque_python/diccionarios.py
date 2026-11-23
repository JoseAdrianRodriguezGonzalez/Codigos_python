### DIccionarions#
#Colección de datos en forma de pares llave valor
#optimizados para recuperar información

#Las llaves son úncias y deben ser no mutables
#El orden de los valores de inserción si importa
d={0:"lunes",
   1:"martes",
   2:"miercoles"}
print(d)
print(d.get(0)) #Regresa la llave si exite, si no, un None
#REgresar otra cosa
print(d.get('s',0))

d[0]='Jueves'
#Si no existe agrega

d[(1,2)]='tupla'

d.update({3:"Jueves",4:"Viernes"})

del d[4]
print(d)

# DIferentes formas en que se puede iterar e un diccioanrio

for keys in d.keys():
    print(keys)
for value in d.values():
    print(value)
for a in d.items():
    print(a)



