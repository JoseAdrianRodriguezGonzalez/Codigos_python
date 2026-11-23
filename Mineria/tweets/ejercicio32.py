"""
@description: Calcular el indice Jaccard entre cada par de usuarios.

Despuś, ecnontrar los dos usuarios más imilares para cada usuario.

"""
import pandas as pd
name_file="tweets_processed"
df=pd.read_csv(name_file+".csv")
tweets=df["texto"].tolist()
users=df['usuario'].unique().tolist()
print(len(users))
def Jaccard(Us1:set,Us2:set):
    return len(Us1.intersection(Us2))/len(Us1.union(Us2))
def get_Words(l_tweets):
    str_u1= " ".join(l_tweets)
    return set(str_u1.split(" "))
diccionario={}
words_users={}
for i, u1 in enumerate(users[:-1]):
    results=[]
    for u2 in users[i+1:]:
        tweet_u1=df[df['usuario']==u1]['texto'].tolist()
        wordset_u1=get_Words(tweet_u1)
        words_users[u1]=wordset_u1
        tweet_u2=df[df['usuario']==u2]['texto'].tolist()
        wordset_u2=get_Words(tweet_u2)
        words_users[u2]=wordset_u2
        # Jaccard
        i_j=Jaccard(wordset_u1,wordset_u2)
        diccionario[(u1,u2)]=i_j

for u1 in users[:5]:
    persona=[]
    for key,value in diccionario.items():
        if u1 in key:
            persona.append((value,key[1]))
    print(u1)
    most_similar=sorted(persona,reverse=True)
    for val in most_similar[:2]:
        print(val)
#Dada una lsita de términos,encontrar el usuario mas most_similar
l_terms=['hola',"mundo"]
s_terms=set(l_terms)
results=[]
print(" ")
for user,set_words in words_users.items():
    results.append((Jaccard(s_terms,set_words),user))
results.sort(reverse=True)
for i in results[:5]:
    print(i)


