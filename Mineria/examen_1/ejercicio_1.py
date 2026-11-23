"""
Nombre: José Adrián Rodríguez González
Curso: Minería de datos
Fecha: 13/10/2025
Descripción: Programa que limpia un texto y lo ordena las frecuencais de las palabras y se escribe en un texto de salida las frecuencias más altas
"""
file_dir="doc.txt"
texto=[]
with open(file_dir,"r",encoding="utf-8") as file:
    for f in file:
       empty=f.lower()
       texto.append(empty)
#print(texto)
limpio=[]
for linea in texto:
    linea=linea.replace(",","").replace(".","").replace(":","").strip()
    limpio.append(linea)
full_text=" ".join(limpio)
full_text=full_text.split(" ")
diccionario={}
for word in full_text:
    diccionario[len(word)]=diccionario.get(len(word),0)+1
elements=sorted([(v,k) for k,v in diccionario.items()],reverse=True)
total_de_palabras=sum([ele[0] for ele in elements])
porcentajes=[(ele[1],ele[0],ele[0]/total_de_palabras) for ele in elements ]
print(porcentajes)

##Now, I'll write it down on another text file
with open("output.txt","w",encoding="utf-8")as file:
    for top in porcentajes[:5]:
        file.write(f"longitud {top[0]}: porcentaje:{top[2]*100:.2f}%\n")
