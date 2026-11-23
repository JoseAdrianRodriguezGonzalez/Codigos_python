"""
Descripcion: Calcular las probabilidades condicionalas para cada una de las palabras en cada categoría de la variable sexo.
"""
import pandas as pd
def getFreqMultinomial(docs):
    d_freq={}
    for d_i in docs:
        l_tokens=d_i.split(" ")        
        for token in l_tokens:
            d_freq[token]=d_freq.get(token,0)+1
    return d_freq

def probMultinomial(d_words):
    multinomial_prob={}
    den=sum(d_words.values())
    for palabra,freq in d_words.items():
        multinomial_prob[palabra]=freq/den
    return multinomial_prob
def getFreqBernoulli(docs):
    d_freq={}
    for d_i in docs:
        s_tokens=set(d_i.split(" "))     
        for token in s_tokens:
            d_freq[token]=d_freq.get(token,0)+1
    return d_freq
def probBernoulli(d_words,n_docs=1):
    bernoulli_prob={}
    for palabra,freq in d_words.items():
        bernoulli_prob[palabra]=freq/n_docs
    return bernoulli_prob


name_file="tweets_processed"
df=pd.read_csv(name_file+".csv")
sexo=df['sexo'].unique()

#Recupara documentos tweets de cada cateooria
d_multinomial= {}
d_bernoulli={}
d_ndocs={}
for c_i in sexo:
    tweets=df[df['sexo']==c_i]['texto'].tolist()
    d_ndocs[c_i]=len(tweets)
    d_multinomial[c_i]=getFreqMultinomial(tweets)
    d_bernoulli[c_i]=getFreqBernoulli(tweets)
#Caluclar probabiidad condicionalas
#multinomial
d_multinomial_prob= {}
d_bernoulli_prob={}
for c_i in d_multinomial:
    d_multinomial_prob[c_i]=probMultinomial(d_multinomial[c_i])
    d_bernoulli_prob[c_i]=probBernoulli(d_bernoulli[c_i],d_ndocs[c_i])

#LAs 5 plabras con mayor porbabilidad para cada exo usando multinomial
for c_i,d_prob in d_multinomial_prob.items():
    lista=sorted([(v,w) for w,v in d_prob.items()])[:-6:-1]
    print(f"Genero {c_i}")
    print(lista)
    
