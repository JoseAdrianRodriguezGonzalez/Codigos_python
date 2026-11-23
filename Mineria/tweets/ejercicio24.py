"""
Usando como base el ejercicio rpevio incluir la elminaciones de palaras vacias

"""
import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
def remove_short_long_words(words):
    words_p=[word for word in words 
             if len(word)>2 and len(word)<21]
    return words_p
def remove_stopwords(words,s_):
    words_=[word for word in words if word not in s_]
    return words_
w_d="tweets.csv"
df=pd.read_csv(w_d)
tweets= df['publicacion'].tolist()
# transformar cada tweet en minuscula
tweets_d=[t.lower() for t in tweets]
print(tweets_d)
# Separa cada publcación en tokens 
#Remover puntos y comas
tweets_p=[ re.findall(r"[a-záéíóúñ]+",t) for t in tweets_d]
print(tweets_p)
tweets_limpios=[remove_short_long_words(tweet_l) for tweet_l in tweets_p]
#Tweets vaciós
vacios=[(ide,limpios) for ide,limpios in  enumerate(tweets_limpios) if len(limpios)==0]
print(vacios)
#promeiods de palabaras por tweet antes de la limpieza
avg=sum(len(tweet) for tweet in tweets_p)/len(tweets_p)
print(avg)
# Despues de la limpiez
avg=sum(len(tweet) for tweet in tweets_limpios)/len(tweets_limpios)
print(avg)

#eliminar palarbas vacías
#nltk.download("stopwords")
stop_words_es=set(stopwords.words("spanish"))

tweets_propor=[remove_stopwords(tweet,stop_words_es) for tweet in tweets_limpios]


vacios=[(ide,limpios) for ide,limpios in  enumerate(tweets_propor) if len(limpios)==0]
print(vacios)
#promeiods de palabaras por tweet antes de la limpieza
avg=sum(len(tweet) for tweet in tweets_p)/len(tweets_p)
print(avg)
# Despues de la limpiez
avg=sum(len(tweet) for tweet in tweets_propor)/len(tweets_propor)
print(avg)

vacios=[(ide,limpios) for ide,limpios in  enumerate(tweets_limpios) if len(limpios)==0]
print(vacios)
#promeiods de palabaras por tweet antes de la limpieza
avg=sum(len(tweet) for tweet in tweets_p)/len(tweets_p)
print(avg)
# Despues de la limpiez
avg=sum(len(tweet) for tweet in tweets_propor)/len(tweets_propor)
print(avg)

print(tweets_propor)
