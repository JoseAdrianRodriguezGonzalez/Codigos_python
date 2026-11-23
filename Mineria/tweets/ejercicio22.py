"""clean = re.sub(r"[!?\¿¡\.,;:]+", "", text)
description : Ler el archivo CSV que contiene los tweets recolectaods y hacer lo siguiente
    - COnvertir los tweets a lista,
    - transformar cada tweet a minúsculas
    - Separar cada publicación en tokens 
"""
import pandas as pd
import re
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
