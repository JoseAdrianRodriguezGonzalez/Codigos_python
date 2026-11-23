import math as mt 
import pandas as pd 
"""
mineria de datos 
1 de diciembre del 2025
Probabilistico 
"""
def unicos(C):
    return set(C)
def extract_vocabualry(D):
    #Esta funcion recibe un docuemtno 
    #Es una funcion que tiene la lista de documentos 
    # Regresa un conjunto con el vocabulario 
    V=[]
    for d in documentos:
        for word in d.split():
            V.append(word)

    return set(V) 
def CountDocsInClass(C,c):
    return sum( 1 for clases in C if clases==c)
def CountDocsInClassContainingTerm(D,C,c,t):
    #ES la lista de documnetos en string 
    #Es la lista de labels en strng 
    #Es la clase que analizamos 
    #Es el termino que buscamos
    documentos_diccionarios={indice:documento for indice,documento in enumerate(D)}
    categorias_diccionarios={indice:categoria for indice,categoria in enumerate(C)}
    D_c={indice:documento for indice,documento in documentos_diccionarios.items() if categorias_diccionarios[indice]==c}
    N_t=sum(1 for documento in D_c.values() if t in documento)
    return N_t 
def train_classifier(D,C):
    #entrenamiento recibe los documentos en strings 
    #y en C en los labels son la lsita de labels 
    c_unicos=unicos(C)
    V=extract_vocabualry(D)
    N=len(D)
    prior={clave:0.0 for clave in c_unicos }
    condprob={palabra: {c_j:0.0 for c_j in c_unicos} for palabra in V}
    for c_j in c_unicos:
        N_c=CountDocsInClass(C,c_j)
        prior[c_j]=N_c/N
        for t in sorted(list(V)):
            N_ct=CountDocsInClassContainingTerm(D,C,c_j,t)
            condprob[t][c_j]=(N_ct+1)/(N_c+2)
    return c_unicos,V,prior,condprob
def extractTermsFromDoc(V,d):
    terminos_d=d.split()
    lista=[termino for termino in terminos_d if termino in V]
    return set(lista)
def testClassifier(C,V,prior,condprob,d):
    #La funcin de evaluacion toma la prior y la condporb para encontrar las pprobabilidades  
    V_d=extractTermsFromDoc(V,d) #Extraigo los terminos del documento de entrar que esten dentro del vocaublairo 
    score={c_j:0.0 for c_j in C}
    for c_j in C:
        score[c_j]=mt.log(prior[c_j])
        for t in sorted(list(V)): #conjunto de los terminos extradiso de d 
            if t in V_d:
                score[c_j]+=mt.log(condprob[t][c_j])
            else:
                score[c_j]+=mt.log(1-condprob[t][c_j])
    lista=sorted([(probabilidad,clase) for clase,probabilidad in score.items()],reverse=True)
    return lista[0][1]
df=pd.read_csv("tweets_processed.csv")
categorias=df["sexo"].to_list()
documentos=df["texto"].to_list() 
c_un,vocabulario,priori,condiprob=train_classifier(documentos,categorias)
clase_predicha=testClassifier(c_un,vocabulario,priori,condiprob,"Hola mundo, a quien pertenzco")
print(clase_predicha)
