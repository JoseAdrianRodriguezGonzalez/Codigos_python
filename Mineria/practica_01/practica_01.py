#Variables librerias globales
from os import read
import re
import pandas as pd
import nltk
import math 
from nltk.corpus import stopwords
nltk.download("stopwords")
data_path="data.txt"
stop_words=set(stopwords.words("spanish"))
"""
Funciones de limpieza de datos
Seccion 2.2 punto 1
"""
def read_data(data_path:str)->dict[int,str]:
    """Función lee un archivo y devuelve su contenido
    Args:
        data_path (str): Es la ruta del archivo a leer 
    Returns:
        dict[int,str]: Devuelve un diccionario con llave entera indicando el índice del documento y el valor un string que es el contenido
    """
    dicc={}
    with open(data_path,"r",encoding="utf-8") as f:
        for idx,line in enumerate(f):
            dicc[idx]=line.strip()
    return dicc
def extraer_alfabeticos(diccionario:dict[int,str])->dict[int,list[str]]:
    """Función que busca y extrae los cáracteres alfabéticos
    Args:
        diccionario (dict[int,str]): Recibe un diccionario con llave entera indicando el indice del documento y el string 
        que es el contenido del documento.
        Además, se hacen minusuclas todas las palabra para facilitar la extracción
        SE recomienda usar estar función despues de usar la función de read_data, ya que se necesita el contenido del documento.
    Returns:
        dict[int,list[str]]: Devuelve un diccionario con clave entera, indiciando el indice de los documentos y
        el valor es una lista de strings. Esto es debido a que por el uso de la librería que extrae caracteres por expresión regugular, retorna
        los elementos extraídos. Suponiendo que se tiene una linea de texto, separar por strings cada vez que encuentra lo que se pide de
        la expresión regular
    """
    diccionario_filtrado={}
    for document in diccionario:
        diccionario_filtrado[document]=re.findall(r'[a-záéíóúñ]+',diccionario[document].lower())
    return diccionario_filtrado
def remover_acentos_string(palabra:str)->str:
    """ESta función remueve los acentos. Recomendablemente se usa después de haber quitado palabras vacías
    Args:
        palabra (str): Plaabra a la que le reemplazará los acentos
    Returns:
        str: Devuelve la palabra sin los acentos
    """
    return palabra.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
def quitar_acentos(diccionario:dict[int,list[str]])->dict[int,list[str]]:
    """Función que quita todos los acentos por documento
    ESta función empaqueta la función remover_acentos_string, para aplicarlar con mayor facilidad a cada palabra
    Args:
        diccionario (dict[int,list[str]]): Es el diccionario con llave entera indicando el indice del documento y los valores
        son los strings de las palabras del documento
    Returns:
        dict[int,list[str]]:Diccionario con mismos indices y los valores son las palabras sin los acentos 
    """
    diccionario_sin_acentos={}
    for documento in diccionario:
        diccionario_sin_acentos[documento]=[remover_acentos_string(palabra) for palabra in diccionario[documento]]
    return diccionario_sin_acentos
def remover_palabras_vacias(diccionario:dict[int,list[str]],stop_words:set[str])->dict[int,list[str]]:
    """Remueve las palabras vacías
    Esta función se debe usar después de extraer los caracteres alfabéticos pero antes de quitar los acentos. Porque los diccionarios de 
    NLTK poseen las palabras vacías con los acentos. 
    Args:
        diccionario (dict[int,list[str]]): Es el ddiccionario con llave entera indicando el indice del documento y los valores
        son las palabras separadas en el documento
        stop_words (set[str]): _description_Es el conjunto de palabras vacías a remover. Se recomienda usar el conjunto proporcionado
        por NLTK

    Returns:
        dict[int,list[str]]: UN diccionario con los mismos indices de entrada. Los valores presentan la misma estructura pero sin
        las palabnras vacías y palabras más cortas de de 3 carácteres o más largas de 20 caracteres
    """
    diccionario_filtrado={}
    for documento in diccionario:
        diccionario_filtrado[documento]=[palabra for palabra in diccionario[documento] if palabra not in stop_words and
                                                                                                2<len(palabra)<21]
    return diccionario_filtrado 
def guardar_resultado(diccionario:dict[int,list[str]],nombre:str):
    """
    _summary_: Función que guarda (recomendablemente en un archivo de texto), el resultado del 
    procesamineto de texto.
    Args:
        diccionario (dict[int,list[str]]): Diccionario con llave entera indicando el indice
        del documento y los valores son listas de strings con las palabras de cada documento procesadas
        nombre (str): Es el nombre del archivo donde se guardará el resultado
    Returns:
        None: No retorna algun tipo de dato, solo escribe el archivo de texto
    """
    with open(nombre,"w",encoding="utf-8") as file:
        for elementos in diccionario.values():
            file.write(f"{" ".join(elementos)}\n")
"""
Seccion 2.2 punto 2
Aqui se hace el llamado de las funcionas anteriormente definidaas
"""
######################################
def juntar_topicos(diccionario:dict[int,str],diccionario_labels_:dict[int,str])->dict[str,list[str]]:
    """Funcion que junta todos los documentos de un mismo topico en un indice

    Args:
        diccionario (dict[int,str]): Diccionario con llave entera indicando el indice dle documento y rel valor el text del documento
        diccionario_labels_ (dict[int,str]): Diccionario con llave entera indicando el indice del documento y el valor el label o topico del documento

    Returns:
        dict[str,list[str]]: Un dccionario con 4 claves que son los topicos y loas valores son los strings de las palabras de cada topico.
    """
    diccionario_vocabulario={}
    for keys,items in diccionario.items():
        diccionario_vocabulario[diccionario_labels_[keys]]=diccionario_vocabulario.get(diccionario_labels_[keys],"")+items+" "
    for keys in diccionario_vocabulario:
        diccionario_vocabulario[keys]=diccionario_vocabulario[keys].split()
    return diccionario_vocabulario
def get_frecuencias(diccionario_completo:dict[str,list[str]])->dict[str,dict[str,int]]:
    """calcula las frecuencias de cada palabra en cada topico

    Args:
        diccionario_completo (dict[str,list[str]]): ES el diccionario Con las claves siendo los topicos(4) y los valores son 
        una lista de strings representando las palabras de cada topico.
    Returns:
        dict[str,dict[str,int]]: Se opbtiene un diccionario con las claves siendo los topicos y los valores son diccionarios
        con las palabras como clave y los valores sus freceucencias
    """
    diccionario_por_topico={}
    for keys,items in diccionario_completo.items():
        diccionario_por_topico[keys]=frecuencias(items)
    return diccionario_por_topico
def frecuencias(palabras:list[str])->dict[str,int]:
    """ES el calculador de frecuencias en base a una lista de palabras

    Args:
        palabras (list[str]): Lista de palabras para calcular las frecuenciaa

    Returns:
        dict[str,int]: LAs frecuencias de cada palabras, siendo la clave la palabra y el valor es la frecuencia. 
    """
    diccionario_frecuencias={}
    for palabra in palabras:
        diccionario_frecuencias[palabra]=diccionario_frecuencias.get(palabra,0)+1
    return diccionario_frecuencias
def sort_frecuencias(diccionario_completo:dict[str,dict[str,int]])->dict[str,list[tuple[int,str]]]:
    """Esta funcion ordena las frecuencias claculadas previamente

    Args:
        diccionario_completo (dict[str,dict[str,int]]): ES el diccionario en el que las claves son los topicos y los valores son las frecuencais de cada palabra, siendo los strings las palabras y el entero es la frecuencia.

    Returns:
        dict[str,list[tuple[int,str]]]: Retorna un diccionario con claves los strings, siendo los topicos, y los valores son listas de tuplas. Cada tupla tiene un entero que es la frecuencia y un string que es la palabra. 
    """
    diccionario_topico={}
    for keys,items in diccionario_completo.items():
        diccionario_topico[keys]=sorted([(frequency,word) for word,frequency in items.items()],reverse=True)
    return diccionario_topico
def write_txt(diccionario:dict[str,list[tuple[int,str]]],cantidad:int):
    """
    _summary_: Escribe un archivo de texto pero en base a la diccionario de las frecuencias ordendas

    Args:
        diccionario (dict[str,list[tuple[int,str]]]): Diccionario con las claves siendo los topicos y los valroes la lsita de tuplas ordenadas por su frecuencia.
        cantidad (int): Cantidad de palabras más frecuentes a escribir por topico 
        ESta funcion no retorna un valor, solo escribe los archivos de palabraas claves y los topicos de las palabras clave como
        keywords.txt y labels_kw.txt.
    """
    
    n=cantidad//2
    with open("keywords.txt","w") as f:
        labels=[]
        for keys,items in diccionario.items():
            palabras_mas_frecuente=items[:cantidad]
            i=0
            while(i<n):
                f.write(f"{palabras_mas_frecuente[i][1]} {palabras_mas_frecuente[i+1][1]} {palabras_mas_frecuente[cantidad-1-i][1]} {palabras_mas_frecuente[cantidad-i-2][1]}\n")
                i+=2
                labels.append(keys)
        with open("labels_kw.txt","w",encoding="utf-8") as file:
            for label in labels:
                file.write(f"{label}\n")
"""
Sección 2.3 punto 1 
DEclarion de funciones
"""
def tf(diccionario:dict[int,str],vocabulario:set[str])->dict[int,dict[int,int]]:

    """Calcula la matriz de frecuencias sparseada, es decir, evitando una matriz con muchos 0, por medio del uso de diccionrios
    Args:
        diccionario (dict[int,str]): Diccionario con llave entera indicando el indice del documento y el valor es el documento completo.
        vocabulario (set[str]): Conjunto de palabras que conformaan el vocabulario, que fue extraido previamente del diccionario.
    Returns:
        dict[int,dict[int,int]]: Devuelve un diccionario con llave entera indicando el indice del documento y el valor es otro diccionario. El diccionario es el indice de la palabra en el vocabulario como la clave y el valor es la frecuencia de la palabra en el documento.  
    """
    diccionario_tf={}
    #ordenar vocabulario y guardarlo en un diccionario 
    vocab_list=sorted(list(vocabulario))
    diccionario_vocabulario={palabra:idx for idx,palabra in enumerate(vocab_list)}
    #Dividir el string en lista de palabras 
    diccionario_spliteado={indice:concepto.split() for indice,concepto in diccionario.items()}
    #Busca la freceuncia de las palabras del vocabulario en cada conecpto 
    for key,palabras in diccionario_spliteado.items():
        diccionario_frecuencias={}
        for palabra in palabras:
            idx=diccionario_vocabulario[palabra]
            diccionario_frecuencias[idx]=diccionario_frecuencias.get(idx,0)+1 
        diccionario_tf[key]=diccionario_frecuencias
    return diccionario_tf
def idf(diccionario:dict[int,str],vocabulario:set[str])->dict[int,float]:
    """Funcion que calcula el vector IDF

    Args:
        diccionario (dict[int,str]): Diccionario con todos los documentos y sus indices
        vocabulario (set[str]):EL vocuablario previamente definido de palabras

    Returns:
        dict[int,float]: Devueleve un diccionario siendo las llaves los indices de la palabras en el vocabulario y los valores es el valor idf por termino. 
    """
    diccionario_idf={}
    #ordenar vocabulario y guardarlo en un diccioanrio 
    vocab_list=sorted(list(vocabulario))
    diccionario_vocabulario={palabra:idx for idx,palabra in enumerate(vocab_list)}
    #Dividir el string en lsita d epalabras 
    diccionario_spliteado={indice:concepto.split() for indice,concepto in diccionario.items()}
    n=len(diccionario_spliteado)
    #buscar la frecuencia de cadapalabra por documento, es decir, en cuantos documentos aparacio 
    frecuencias_documento={i:0 for i in range(len(vocab_list))}
    for palabras in diccionario_spliteado.values():
        palabras_unicas=set(palabras)
        for palabra in palabras_unicas:
            idx=diccionario_vocabulario[palabra]
            frecuencias_documento[idx]+=1 
    diccionario_idf={palabra:math.log(n/frecuencia) for palabra,frecuencia in frecuencias_documento.items()}
    return diccionario_idf
    
def getVocabulary(diccionario:dict[int,str])->set[str]:
    """Se obtiene o crea el vocabulario a partir de un diccionario

    Args:
        diccionario (dict[int,str]): Claves que son los indices de los documentso y los documentos ocmo valores.

    Returns:
        set[str]: Representa el conjunto de palabras unicas extraidas del diccionario.
    """
    diccionario_div={}
    for keys,values in diccionario.items():
        diccionario_div[keys]=values.split()
    conjunto=set()
    for keys,values in diccionario_div.items():
        conjunto=conjunto.union(set(values))
    return conjunto 
def TF_IDF(tf:dict[int,dict[int,int]],idf:dict[int,float])->dict[int,dict[int,float]]:
    TFIDF_d={i:{} for i in tf}
    for documento,frecuencia in tf.items():
        TFIDF_d[documento]={palabra:freq*idf[palabra] for palabra,freq in frecuencia.items() }
    return TFIDF_d 
def norm_l2(vector:dict[int,float])->float:
    return (sum(v**2 for v in vector.values()))**0.5
def vector_normal(vector:dict[int,float])->dict[int,float]:
    norma=norm_l2(vector)
    return {indice:v/norma for indice,v in vector.items()}
def normalizar(tfidf:dict[int,dict[int,float]])->dict[int,dict[int,float]]:
    return {indice:vector_normal(documento) for indice,documento in tfidf.items()}
"""
Seccion 2.3 punto 2 
funciones 
"""
def tfidf_keywords(ruta_keywords:str,vocabulario:set[str],idf:dict[int,float])->dict[int,dict[int,float]]:
    """
    _summary_: Calcula los vectores TF-IDF normalziados con la norma euclideana para las tuplas de las palabras clave 
    Args:
        ruta_keywords (str): Es la ruta del archivo que contiene las palabras clave
        vocabulario (set[str]): Es el conjunto de palabras que conforman el vocabualrio, extraidop peviamente dlke diccionario completo
        idf (dict[int,float]): Es el diccionario que contiene los valores IDF por palabra. Pudo haber sido otra estructura como una lista, pero se definio el usuario para mantener la consistencia en la mayoria de documentos.
    Returns:
        dict[int,dict[int,float]]: Devuelve un diccionario con la calves siendo el indice de la tupla de pabras calaves y los valroes son un diccionario convertido a idf. Siendo el valor entero el inidice de las palabras y el flotante es el valor idf.
    """
    lista_vocabulario=sorted(list(vocabulario))
    diccionario_vocabulario={palabra:idx for idx,palabra in enumerate(lista_vocabulario)}
    vectores={}
    with open(ruta_keywords,"r",encoding="utf-8") as f:
        for idx,linea in enumerate(f):
            palabras=linea.strip().split() 
            tfidf={diccionario_vocabulario[palabra]:idf[diccionario_vocabulario[palabra]] for palabra in palabras}
            tfidf_normalizado=vector_normal(tfidf)
            vectores[idx]=tfidf_normalizado
    return vectores 

"""
Seccion 2.3 punto 3
Funciones 
"""
def similitud_coseno(u1:dict[int,float],u2:dict[int,float])->float:
    """Similitud coseno

    Args:
        u1 (dict[int,float]): es el vector normalizado con la norma euclideana
        u2 (dict[int,float]): otro vector normalziado con la norma euclideana

    Returns:
        float: Devuevle el valor de la similitud coseno.
    """
    keys=set(u1).intersection(set(u2))
    d=sum( u1[k]*u2[k] for k in keys )
    return d 
def tuplas_documentos_coseno(documentos:dict[int,dict[int,float]],tuplas:dict[int,dict[int,float]]):
    """Aplica la similitud coseno a cada uno de las tuplas y cada uno de los documentos
    Args:
        documentos (dict[int,dict[int,float]]): el diccionario de documentos convertidos a matriz TF-IDF normalziada
        tuplas (dict[int,dict[int,float]]): El diccionario de tuplas de los keywrods convertidos a matriz TF-IDF normalziada

    Returns:
        dict[int,dict[int,float]]: Devuelve un diccionario con los indices de las tuplas como claves y los valores son un diccionario, siendo el indicie del documento como clave y el valor es la similitud coseno entre la tupla y el documento.
    """
    distancias_={}
    for tupla,vector2 in tuplas.items():
        distancias={}
        for documento,vector1 in documentos.items():
            d=similitud_coseno(vector1,vector2)
            distancias[documento]=d
        distancias_[tupla]=distancias
    return distancias_
def ordernar_tuplas(distancias_por_tuplas:dict[int,dict[int,float]])->dict[int,list[tuple[float,int]]]:
    """
    _summary_: Se ordena cada tupla las distancias que tienen con cada documento
    Args:
        distancias_por_tuplas (dict[int,dict[int,float]]): Diccionario que fue calculado con la anterior funcion, las claves son la tuplas y el valor es el diccionario con la clave como indice del documetno y el valor la similitud coseno.
    Returns:
        dict[int,list[tuple[float,int]]]: Devuelve un diccionario con las claves como los indices de las tuplas y los valores son la slistas de las tuplas. Siendo el el flotante la frecuencia y el entero el indice del documento.
    """
    guardar_resultado={}
    for tupla,distancias in distancias_por_tuplas.items():
        lista=sorted([(distancia, documento) for documento,distancia in distancias.items() ],reverse=True)
        guardar_resultado[tupla]=lista 
    return guardar_resultado 
"""
Seccion 2.3 punto 4

"""
def escribir(distancias_tuplas:dict[int,list[tuple[float,int]]],cantidad:int):
    """
    _summary_: Escribe un archivo de texto con los resultados de las tuplas y los documentos más parecidos o cercanos
    Args:
        distancias_tuplas (dict[int,list[tuple[float,int]]]): Diccionario con las claves como el indiice de la sutplas y los valores
        son los las listas de tuplas, siendo el valor flotante como la frecuencia y el valor entero es el indice del documento.
        cantidad (int): Cantidad de documentos más cercanos a escribir por tupla
    Esta funcion no retorna algun valor, solo escribe el archivo de texto llamado results.txt"""
    with open("labels.txt","r",encoding="utf-8") as file:
        labels_documentos=[f.strip() for f in file]
    with open("labels_kw.txt","r",encoding="utf-8") as file:
        labels_tuplas=[ f.strip() for f in file]
    with open("keywords.txt","r",encoding="utf-8") as file:
        tuplas_texto=[f.strip() for f in file]
    with open("results.txt","w",encoding="utf-8") as file:
        texto=""
        for tupla,distancias in distancias_tuplas.items():
            distancias_cercanas=[documento for _,documento in  distancias[:cantidad]]
            topicos_documento=[labels_documentos[documento] for documento in distancias_cercanas]
            texto=f"{tuplas_texto[tupla]}; {labels_tuplas[tupla]}; {distancias_cercanas}; {topicos_documento}\n"
            file.write(texto)
"""Seccion 2.4 punto
FUnciones 
""" 

def precision_recall(resultados: str)->tuple[list[float],list[float]]:
    """Calcula por cada tupla el precision y el recall

    Args:
        resultados (str):Es el nombre del archivo de texto que contiene los resutlados de la distancia coseno y su cercania con cada tupla, este fue definido en la anterior funcion escribir.

    Returns:
        tuple[list[float],list[float]]: ES una tupla de valores con dos listas, sineod la primera los valores del precision y la seugnda con los valores del recall.
    """
    lista_precision=[]
    lista_recall=[]
    with open("labels.txt", "r", encoding="utf-8") as f:
        lista = [label.strip() for label in f]
    with open(resultados, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.split(";")
            linea=[l.strip() for l in linea]
            topico_tupla=linea[1]
            topicos_documentos=linea[3]
            lista_documentos=topicos_documentos.replace("[","").replace("]","").replace("'","").split(",")
            lista_documentos=[topico.strip() for topico in lista_documentos]
            precision_tupla=precision(topico_tupla,lista_documentos)
            recall_tupla=recall(topico_tupla,lista_documentos,lista)
            lista_precision.append(precision_tupla)
            lista_recall.append(recall_tupla)
    return lista_precision,lista_recall 
def precision(topico_tupla:str,lista_documentos:list[str])->float:
    """Funcion que calcula la precision

    Args:
        topico_tupla (str): el topico de la tupla
        lista_documentos (list[str]): La lista e documentos recuperados

    Returns:
        float: El valor del precision 
    """
    numerador=sum([1 for topicos in lista_documentos if topico_tupla== topicos])
    return numerador/len(lista_documentos)
def recall(topico_tupla:str,lista_documentos:list[str],lista_relevante:list[str])->float:
    """
    Funcion que calcula la precision

    Args:
        topico_tupla (str): el topico de la tupla
        lista_documentos (list[str]): La lista e documentos recuperados
        lista_relevante (list[str]): La lista que contiene los documentos con el mismo topico de la tupla.
        Siempre deben de ser 20

    Returns:
        float: El valor del recall
    """  
    numerador=sum([1 for topicos in lista_documentos if topico_tupla == topicos])
    documento_relevante=sum(1 for topico in lista_relevante if topico_tupla==topico)
    return numerador/documento_relevante
"""     
Seccion 2.2 punto 1
Llamada de funciones de limpieza de datos
"""
documentos=read_data(data_path)
 
documentos_limpios=extraer_alfabeticos(documentos)
documento_sin_palabras_vacias=remover_palabras_vacias(documentos_limpios,stop_words)
documentos_sin_acentos=quitar_acentos(documento_sin_palabras_vacias)
guardar_resultado(documentos_sin_acentos,"data_processed.txt")
"""
2.2 punto 2
"""
data_processed="data_processed.txt"
labels="labels.txt"
diccionario_procesado=read_data(data_processed)
diccionario_labels=read_data(labels)
diccionario_topicos=juntar_topicos(diccionario_procesado,diccionario_labels)
diccionario_frecuencias=get_frecuencias(diccionario_topicos)
diccionario_frecuencias_ordenadas=sort_frecuencias(diccionario_frecuencias)
write_txt(diccionario_frecuencias_ordenadas,60)

"""
Sección 2.3 punto 1 
llamada de funciones 
"""
#VOy a utilizar los diccionarios de la svariables 103 y 102
vocabulario=getVocabulary(diccionario_procesado)
diccionario_tf=tf(diccionario_procesado,vocabulario)
diccionario_idf=idf(diccionario_procesado,vocabulario)
diccionario_vectores_TFIDF=TF_IDF(diccionario_tf,diccionario_idf)
diccionario_vectores_TFIDF_normalizado=normalizar(diccionario_vectores_TFIDF)
#print(diccionario_vectores_TFIDF_normalizado)
"""
Sección 2.3 punto 2
llamada de funciones 
"""
matriz_tfidf_tuplas=tfidf_keywords("keywords.txt",vocabulario,diccionario_idf)
"""
Seccion 2.3 punto 3
llamadas  
"""
diccionario_tuplas_distancias=tuplas_documentos_coseno(diccionario_vectores_TFIDF_normalizado,matriz_tfidf_tuplas)
diccionario_tuplas_cercanas=ordernar_tuplas(diccionario_tuplas_distancias)
escribir(diccionario_tuplas_cercanas,5)
"""Seccion 2.4 punto
FUnciones 
"""
precision_l,sensibilidad_l=precision_recall("results.txt")
print(f"El promedio de la metrica de precision: {sum(precision_l)/len(precision_l)}")
print(f"El promedio de la metrica de recall: {sum(sensibilidad_l)/len(sensibilidad_l)}")
