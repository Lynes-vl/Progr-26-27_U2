lista = ["hola", "Pepe", "xd", "Manolo", "Hola", "xd"]
def ListaSinRepetir(lista):
    listaSinRep = []
    for palabra in lista:
        if palabra not in listaSinRep:
            listaSinRep.append(palabra)
    return listaSinRep

print(ListaSinRepetir(lista))