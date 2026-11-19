def media(lista):
    x=0
    for i in lista:
        x+=i
    x=x//len(lista)
    return x

def pares(lista):
    x=0
    for i in lista:
        if i%2==0:
            x+=1
    return x

def negativos(lista):
    x=0
    for i in lista:
        if i<0:
            x+=1
    return x

def suma(lista):
    x=0
    for i in lista:
        x+=i
    return x


lista=[]
for i in range(1,6):
    lista.append(int(input(f"Dame un númeto {i}/5: ")))

print(f"La media es {media(lista)}.")
print(f"Hay {pares(lista)} número pares.")
print(f"Hay {negativos(lista)} números negativos.")
print(f"La suma es {suma(lista)}.")

