"""
Descripcion:Leer los datos recolectaods y para la variable sexo
"""
import pandas as pd
w_d="./"
i_f=w_d+'info_estudiantes.csv'

df=pd.read_csv(i_f)

freq=df["sexo"].tolist()
freq_filter=[i.lower().strip()  for i in freq]
print(freq_filter)
h_count=freq_filter.count("h")
m_count=freq_filter.count("m")



print(f"Hay {h_count} hombres->{h_count/len(freq_filter):.2f}")
print(f"Hay {m_count} mujeres->{m_count/len(freq_filter):.2f}")


# Segunda forma

unique =list(set(freq_filter))
l_count=[freq_filter.count(i) for i in unique]
for v,f in zip(unique,l_count):
    print(f"Hay {f}{v} -> {f/sum(l_count)}") 


#Tercera forma
d={}
for elemento in freq_filter:
    d[elemento]=d.get(elemento,0)+1
for k,v in d.items():
    print(f'Hay {v} {k}-> {v/sum(d.values())}')
