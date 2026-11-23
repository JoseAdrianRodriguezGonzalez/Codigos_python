"""
Description : tomando como bsa el ejmplo anterior Eliminar secuencias de caractreses alfabéticos de menos de 3 cáracteres y má de 20 caracteres,
"""
import pandas as pd
import re
def remove_short_long_words(words):
    words_p=[word for word in words 
             if len(word)>2 and len(word)<21]
    return words_p
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
