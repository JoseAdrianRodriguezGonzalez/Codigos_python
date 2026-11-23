"""
description: Generar una nube de palabras para cada valor posible en la colymna sexo
Ademas encontrar las palabras que tienen en comun

"""
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
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
sexo=df["sexo"].tolist()
tweets=[tweet.split(" ") for tweet in tweets]
tweet_m=[]
tweet_h=[]
for s,t in zip(sexo,tweets):
    if s=="hombre":
        tweet_h.append(t)
    else:
        tweet_m.append(t)
freq_hombre=freq_words(tweet_h)
freq_mujeres=freq_words(tweet_m)
wordcl=WordCloud(max_words=50,background_color="white",width=1024,height=1024)
wordcl.generate_from_frequencies(freq_hombre)
plt.figure()
plt.imshow(wordcl,interpolation='bilinear')
plt.axis("off")
plt.savefig("wordcloud.pdf")
plt.show()


wordcl=WordCloud(max_words=50,background_color="white",width=1024,height=1024)
wordcl.generate_from_frequencies(freq_mujeres)
plt.figure()
plt.imshow(wordcl,interpolation='bilinear')
plt.axis("off")
plt.savefig("wordcloud.pdf")
plt.show()
voc_h=" ".join([" ".join(tweet) for tweet in tweet_h])
print(voc_h)

