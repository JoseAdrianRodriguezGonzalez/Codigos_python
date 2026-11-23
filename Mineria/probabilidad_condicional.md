$P(A|B)=\frac{P(A\cap B )}{P(B)}$
$P(w_i|c_j)=\frac{P(w_i \cap c_j)}{P(c_j)}$

Multinomial

$P(w_i|c_j)=\frac{N_wi,cj}{\sum_{w_k \in V}N_{w_k,c_j}}$ 
EL numeroador es el numero de aparicion de $w_i$ en los docmentos de $C_j$

Bernoulli
$P(w_i|c_j)=\frac{N_i,d_j}{N_dj}$
#En cuantos documentos aparece la palaaba $w_j$ es el numerador
el denominador es la cantidad total de documentos

# Bayes

$P(A|B)=P(B|A)P(A)*P(A)/p(B)$
A prori P(A)
Probabilidad totla P(B)
Verosimilitud P(B|A)


Para palabras $P(c_j|d)=P(d|c_j)P(c_j)/P(d)$

ES proporocional $P(c_j|d)$ a $P(d|c_j)P(c_j)$

La probabilidad que haya una palabra dado a  una clase
siendo $d=[w_1,w_2,w_3,\cdots,w_n]$

$P(c_j|w_1,...,w_n) \propto P(w_1,...w_n|c_j)P(c_j)$
ESto tambie es igual $P(w_1,c_j)P(w_2|c_j)...p(w_n|c_j)P(c_j)$

A su vez $P(c_j|d)\propto P(c_j) \prod_{i=1}P(w_i|c_j)$

ASi se encuentra a que clase esa una palabra $argmax(P(c_j|d))_{c_j \in C}$

Si le aplicamos logaritmos

$log(P(c_j|d)) \propto log(P(c_j)) +\sum^K_{i=1}P(w_i|c_j)$

$argmax_{c_j\in C} [log P(c_j)+\sum_{i=1}^k log((P(w_i|c_j))]$

Podemos añadir un 1 Tanto arriba como abajo de la multinomial


$P(w_i|c_j)=\frac{N_wi,cj+1}{\sum_{w_k \in V}N_{w_k,c_j}+1} $


$P(w_i|c_j)=\frac{N_wi,cj+\alpha}{\sum_{w_k \in V}N_{w_k,c_j}+\alpha |V|} $

Bernoulli


$P(w_i|c_j)=\frac{N_i,d_j+1}{N_dj+2}$
