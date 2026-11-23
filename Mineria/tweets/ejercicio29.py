"""
Descripción: Usando el archivo tweets_procesed.csv, genrar un gráfico de barras con las 15 palabras más comunes
    """
import pandas as pd
import matplotlib.pyplot as plt
def freq_words(docs):
    dicti={}
    for doc in docs:
        for word in doc:
            dicti[word]=dicti.get(word,0)+1
    return dicti
def freq_tweet(docs):
    dicti={}
    for doc in docs:
        for word in set(doc):
            dicti[word]=dicti.get(word,0)+1
    return dicti
name_file="tweets_processed"
df=pd.read_csv(name_file+".csv")
tweets=df["texto"].tolist()
for tweet in tweets:
    if "bla bla" in tweet:
        print(tweet)
tweets=[tweet.split(" ") for tweet in tweets]
frecuencias=freq_words(tweets)
print(frecuencias)
l_freq=sorted([(frecuencia,palabra) for palabra,frecuencia in frecuencias.items()],reverse=True)
words=[t[1] for t in l_freq[:15]]
freq=[t[0] for t in l_freq[:15]]
tweets_freq=freq_tweet(tweets)
t_freq=sorted([(frecuencia,palabra) for palabra,frecuencia in tweets_freq.items()],reverse=True)
words_t=[t[1] for t in t_freq[:15]]
freq=[t[0] for t in t_freq[:15]]

plt.figure()
plt.bar(words,freq)
plt.xticks(rotation=90)
plt.title("LAs 15 palabras mas frecuentes")
plt.xlabel("palabras")
plt.ylabel("frecuencias")
plt.show()
plt.figure()
plt.bar(words_t,freq)
plt.xticks(rotation=90)
plt.title("LAs 15 palabras mas frecuentes por tweet")
plt.xlabel("palabras")
plt.ylabel("frecuencias")
plt.show()

