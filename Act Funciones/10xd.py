def hora(s):
    h=s//3600
    return h

def minuto(s):
    mi=(s%3600)//60
    return mi

def segundo(s):
    s=(s%3600)%60
    return s


def total(t): 
    h=hora(t)
    mi=minuto(t)
    s=segundo(t)
    return [h,mi,s]

tiempo=int(input("Dame los s que pasar a h,min y s: "))
horas=hora(tiempo)
print(horas)
minutos=minuto(tiempo)
print(minutos)
segundos=segundo(tiempo)
print(segundos)
