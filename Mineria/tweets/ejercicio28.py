"""
Description: Tomando como base el ejercicio previo crear un archvivo csv conjunto de datos procesados 
"""
#elimianr palabras vacias 
import pandas as pd 
import nltk
import re
from nltk.corpus import stopwords
nltk.download("stopwords")
def vocab(docs):
    voc=set()
    for doc in docs:
        for word in doc:
            if word not in voc:
                voc.add(word)
    return voc
def freq_words(docs):
    dicti={}
    for doc in docs:
        for word in doc:
            dicti[word]=dicti.get(word,0)+1
    return dicti
def replace_accents(words):
    word_p=words.replace("á","a").replace("é","e")
    word_p=word_p.replace("í","i").replace("ó","o")
    word_p=word_p.replace("ú","u")
    return word_p
def remove_short_long_words(words):
    words_p=[word for word in words
             if len(word)>2 and len(word)<21]
    return words_p
def remove_stopwords(words,s_):
    words_=[word for word in words if word not in s_]
    return words_

def preproc_doc(doc,s_w):
    #doc='hola ,mundo'
    #1.Obtener tokens palabras del documento
    doc=re.findall(r'[a-záéíóúñ]+',doc.lower())
    #2 ELimianr palabras muy cortas o muy largas
    doc=remove_short_long_words(doc)
    #3 Remover palabras vacias
    doc=remove_stopwords(doc,s_w)
    #4 remover acentos
    doc=[replace_accents(word) for word in doc]
    return doc
w_d="tweets.csv"
#leer tweets
df=pd.read_csv(w_d)

#convertir los tweets a lista
tweets=df['publicacion'].tolist()
user=df["usuario"].tolist()
#llamar a los stepwrords
stop_words_es=set(stopwords.words("spanish"))
tweets_p=[preproc_doc(tweet,stop_words_es) for tweet in tweets]
vocab_final=freq_words(tweets_p)
#la palabra mas frecuente es
order=[(freq,word) for word, freq in vocab_final.items()]
order.sort()
word=order[-1][1]
freq=order[-1][0]
print(f'Palabra mas frecuente es {word} con {freq}')
counter=0
for tweet in tweets_p:
    if word in tweet:
        counter+=1
print(counter)
sexo=df['sexo'].tolist()
print(sexo)
sex_p=[re.findall(r"[a-z]+",s) for s in sexo]
sex_p=["".join(lista) for lista in sex_p]
print(sex_p)
user_f=[]
sex_f=[]
tweets_f=[]
for u,s,t in zip(user,sex_p,tweets_p):
    if len(t)>0:
        user_f.append(u)
        sex_f.append(s)
        tweets_f.append(" ".join(t))
df_1=pd.DataFrame({"usuario":user_f,"sexo":sex_f,"texto":tweets_f})
df_1.to_csv("tweets_processed.csv",index=False)

