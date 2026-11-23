import pandas as pd
"""
mineria de datos 
1 de diciembre del 2025
geoemtrico
"""

def extract_vocabualry(D):
    #Esta funcion recibe un docuemtno 
    #Es una funcion que tiene la lista de documentos 
    # Regresa un conjunto con el vocabulario 
    V=[]
    for d in D:
        for word in d.split():
            V.append(word)

    return set(V) 
def select_K(d_prima,C):
    return 3 
def transform(D,V):
    #Transformo la lsita de docuemtno
    #A una representaicon numerica con una base de vocabulario 
    #rETORNA lo vectores esparseados 
    vocabulario_numerico={palabra:idx for idx,palabra in enumerate(sorted(list(V)))}
    diccionario={idx:{} for idx in range(len(D)) }
    for indice,documento in enumerate(D):
        vector_sparseado={}
        for palabra in documento.split():
            indice=vocabulario_numerico[palabra]
            vector_sparseado[indice]=vector_sparseado.get(indice,0)+1
        diccionario[indice]=vector_sparseado
    return diccionario 
def train_Classifier(D,C):
    #ESta funcion recibe los documentos en formato de lista de strings 
    #EL C es el valor de la clase que proviene de sexo 
    V=extract_vocabualry(D)
    D_prime=transform(D,V)
    k=select_K(D_prime,C)
    return D_prime,V,k
def TransformDocument(d,V):

    # Transofrom el documento de entrada que es un string 
    # A una representación numerica 
    vocabulario_numerico={palabra:idx for idx,palabra in enumerate(sorted(list(V)))}
    vector_sparseado={}
    for word in d.split():
        indice=vocabulario_numerico.get(word,0)
        vector_sparseado[indice]=vector_sparseado.get(indice,0)+1
    return vector_sparseado
def unicos(C):
    return set(C)
def normalizar(v):
    #Recib un vector 
    return (sum(x**2 for x in v.values()))**0.5 
def distancia_coseno(v1,v2):
    u1={indice:x/normalizar(v1) for indice,x in v1.items()}
    u2={indice:x/normalizar(v2) for indice,x in v2.items()}
    d=0
    claves=set(u1.keys()).intersection(set(u2.keys()))
    for indices in claves:
        d+=u1[indices]*u2[indices]
    return 1-d 
    # 1-u_1*u_2
def computeNearestNeighbors(dp,Dp,k):
    diccionario={documentos:0 for documentos in Dp.keys()}
    for indice,documentos in Dp.items():
        #INdice del documento 
        #documentos es el vector con indices de las palabras y las frecuencias 
        diccionario[indice]=distancia_coseno(dp,documentos)
    #Ordenar y tomar solo los k mas cercanos 
    lista_ordenada=sorted([(distancias,indice) for indice,distancias in diccionario.items()])
    return lista_ordenada[:k]
def DocumentosFromClass(C,c_j):
    #C es una lista de caraceristicas
    #c_j es la calse que debe de extraer, su indice en escencia 
    return [indice for indice,categoria in enumerate(C) if categoria==c_j]
def evaluacion(S_k,D_j,k):
    #S_k es la lista de indices y frecuencais mas cercanas (distancia,indice) 
    #D_j es la lista de indices que le corresponden a la clase 
    #k es la longitud de S_k 
    cardinalidad=sum(1 for distancia,indice in S_k if indice in D_j )
    return cardinalidad/k 
def test_classifier(Dp,C,V,k,d):

    dp=TransformDocument(d,V)
    c=unicos(C)
    documentos_mas_cercanos=computeNearestNeighbors(dp,Dp,k)
    p=[]
    for c_j in c:
        D_j=DocumentosFromClass(C,c_j) #lista de indiices por documento 
        p_j=evaluacion(documentos_mas_cercanos,D_j,k)
        p.append((p_j,c_j))
    return sorted(p,reverse=True)[0][1]



    




df=pd.read_csv("tweets_processed.csv")
categorias_=df["sexo"].to_list()
documentos_=df["texto"].to_list() 
Dp,V,k=train_Classifier(documentos_,categorias_)
clase=test_classifier(Dp,categorias_,V,k,"hola mundo esta es una prueba")
print(clase)
"""
Geometric classifier
"""

