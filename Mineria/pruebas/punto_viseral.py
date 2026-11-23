"""
DEscription: implementar un función para calcuarl al correlación unto-biseral.
"""

def coeff_bi(cont_var,cat_var,group_1):
    coeff=0
    n=len(cont_var)
    n1=cat_var.count(group_1)
    n0=n-n1
    m1=sum(x for x,y in zip(cont_var,cat_var )if y==group_1)
    m2=sum(x for x,y in zip(cont_var,cat_var )if y!=group_1)
    m=sum(cont_var)/n
    var=sum((x-m)**2 for x in cont_var)/(n-1)
    std=var**0.5
    return ((m1-m2)/std) *(n1*n0/n**2)**0.5
calificaciones=[6,6,6,7,10,10]
sexo=["h","h","h","h","m","m"]
coeff=coeff_bi(calificaciones,sexo,"h")
print(coeff)
