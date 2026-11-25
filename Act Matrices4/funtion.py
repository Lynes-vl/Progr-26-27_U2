def celda(matriz,fila,columna):
    return matriz[fila][columna]

def fila(matriz,fila):
    return matriz[fila]

def imprimirColumna(matriz,columna):
    for i in matriz:
        print(i[columna])

def sumaMatriz(matriz):
    total=0
    for x in matriz:
        for y in x:
            total += y
    return total

def separaPares(matriz):
    pares = []
    for fila in matriz:
        for i in fila:
            if i % 2 == 0:
                pares.append(i)
    return pares

def sumaFila(matriz,fila):
    suma = 0
    for i in matriz[fila]:
        suma += i
    return suma