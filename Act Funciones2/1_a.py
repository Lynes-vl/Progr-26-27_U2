def a(lista):
    contador=0
    for i in range(len(lista)):
        for x in lista[i]:
            if x== "a":
                contador+=1
    print(f"Aparece la letra \"a\" {contador} veces")

x=input("Dame tu nombre completo: ").split()
a(x)



