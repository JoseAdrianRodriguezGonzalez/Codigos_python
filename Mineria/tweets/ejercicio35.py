"""
CALCULAR DISTANCIAS YSABD LA MATRIZ DOCUMENTO TERMINO
"""
import pandas as pd
import time 
def getVocabulary(docs):
    V=set()
    for d in docs:
       V= V.union(set(d))
    return V
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

v1=matrix_dt[0]
v2=matrix_dt[-1]
print(euclideanDistance(v1,v2))
