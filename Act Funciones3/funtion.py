def f1(lista):
    for i in lista:
        print(i)

def f2(lista):
    for i in lista[::-1]:
        print(i)

def f3(lista):
    for i in lista:
        print(i[::-1])

def dameColumna(matriz,num):
    print(matriz[num])

def imprimir(lista):
    for x in lista:
        fila=""
        for y in x:
            fila+=f"{y}"
        print(fila)

def estaOrdenadaAscendemente(lista):
    for i in range(0,len(lista)-2):
        if lista[i]>lista[i+1]:
            return False
    return True