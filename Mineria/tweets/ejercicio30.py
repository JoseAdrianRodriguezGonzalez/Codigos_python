"""
Crear una nube de palabras

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
for tweet in tweets:
    if "bla" in tweet:
        print(tweet)
tweets=[tweet.split(" ") for tweet in tweets]
frecuencias=freq_words(tweets)
tweets_freq=freq_tweet(tweets)
wordcl=WordCloud(max_words=50,background_color="white",width=1024,height=1024)
wordcl.generate_from_frequencies(frecuencias)
plt.figure()
plt.imshow(wordcl,interpolation='bilinear')
plt.axis("off")
plt.savefig("wordcloud.pdf")
plt.show()
