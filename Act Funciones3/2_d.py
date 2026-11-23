lista=[[8,1,6],[3,5,7],[4,9,2]]

def imprimeMatrizInvertida(lista):
    for i in range(len(lista)):
        print(f"{lista[i]}     {lista[-i-1][::-1]}")

imprimeMatrizInvertida(lista)