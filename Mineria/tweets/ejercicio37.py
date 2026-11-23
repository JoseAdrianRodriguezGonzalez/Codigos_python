
import pandas as pd
import time
def cosineDistance(v1,v2):
    cosine_similarity=0
    s_keys=set(v1.keys()).intersection(v2.keys())
    for key in s_keys:
        cosine_similarity+=v1[key]*v2[key]
    return 1-cosine_similarity
def getVocabulary(docs):
    V=set()
    for d in docs:
       V= V.union(set(d))
    return V
def euclideanNorm(vector):
    norm=sum(v**2 for v in vector.values())
    return norm**0.5
def euclideanDistance(v1,v2):
    K=set(v1.keys()).union(v2.keys())
    d=0
    for key in K:
        d+=(v1.get(key,0)-v2.get(key,0))**2
    return d**0.5
name_file="tweets_processed"
df=pd.read_csv(name_file+".csv")
tweets=df['texto'].to_list()
#COnvertir acada tweet a una lista de palabras
tweets=[tweet.split(' ') for tweet in tweets]
#Obtener vocabulario 
V=getVocabulary(tweets)
#INdexar vocabulario 
V_s=sorted(list(V))
voc_idx={w:i for i,w in enumerate(V_s)}
matrix_dt=[]
t=time.time()
for tweet in tweets:
    vector={}
    for w in tweet:
        idx=voc_idx[w]
        vector[idx]=vector.get(idx,0)+1
    matrix_dt.append(vector)
#Calcular idf(t)
#idf(t)=log(n/df(t))
#donde t es una palabara en V_s#df(t)=#docs que contieneen a texto
n=len(matrix_dt)
df_t={}
for t in V:
    idx_t=voc_idx[t]
    for documentos in matrix_dt:
        if idx_t in documentos:
            df_t[idx_t]=df_t.get(idx_t,0)+1
#2 calcular idf(tt)
import math as mt 
idf={}

for t in V:
    idx_t=voc_idx[t]
    idf[idx_t]=mt.log(n/df_t[idx_t])
#3) TF-IDF
tf_idf=[]
for vector in matrix_dt:
    vetor_nuevo={i:f*idf[i] for i,f in vector.items()}
    tf_idf.append(vetor_nuevo)
#4) normalizar los vectores 
l_norm=[]
for vector in tf_idf:
    norm=euclideanNorm(vector)
    vector_n={i:f/norm for i,f in vector.items()}
    l_norm.append(vector_n)
