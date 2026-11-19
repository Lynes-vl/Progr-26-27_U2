def a(lista):
    contador=0
    for i in range(len(lista)):
        for x in lista[i]:
            if x== "a":
                contador+=1
    return contador

x=input("Dame tu nombre completo: ").split()
print(f"Aparece la letra \"a\" {a(x)} veces")