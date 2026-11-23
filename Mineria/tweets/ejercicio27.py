

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
# EN cuantos teweets aparecen las palabras 5 mas frecuente
top_5=order[-5:]
diccio={}
for _,palabra in top_5:
    count=sum(1 for tweet in tweets_p if palabra in tweet)
    diccio[palabra]=count
print(diccio)
print(len(tweets_p))
