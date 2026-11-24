lista=[[8,1,6],[3,5,7],[4,9,2]]

def imprimir(lista):
    for x in lista:
        fila=""
        for y in x:
            fila+=f"{y}"
        print(fila)

imprimir(lista)