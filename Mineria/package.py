"""
This will contain several fnctions that can be useful at its usage in different approaches
First of all, we can make a function that can calculate the frequency 
    """
def frequency(lista:iter):
    freq=dict()
    for i in lista:
        freq[i]=freq.get(i,0)+1
    sorted_dict={k:v for k,v in sorted(freq.items(),key=lambda x:x[1],reverse=True)}
    return freq,sorted_dict
