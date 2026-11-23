"""
Obtener matriz de 
"""
import pandas as pd
import time 
def getVocabulary(docs):
    V=set()
    for d in docs:
       V= V.union(set(d))
    return V 
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
for tweet in tweets:
    vector=[]
    for palabra,idx  in voc_idx.items():
        vector.append(tweet.count(palabra))
    matrix_dt.append(vector)
#Manejando dispersion
matrix_dt_2=[]
t=time.time()
for tweet in tweets:
    vector={}
    for w in tweet:
        idx=voc_idx[w]
        vector[idx]=vector.get(idx,0)+1
    matrix_dt_2.append(vector)
print(matrix_dt_2)
#Reconstruir tweet en base a su vector


