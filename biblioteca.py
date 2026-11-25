def suma(x,y):
    return x+y

def resta(x,y):
    return x-y

def ListaSinRepetir(lista):
    listaSinRep = []

    for palabra in lista:
        if palabra not in listaSinRep:
            listaSinRep.append(palabra)

    return listaSinRep
