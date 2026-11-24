def estaOrdenadaAscendemente(lista):
    valor = True
    pos=0
    while pos<len(lista)-2 and valor:
        if lista[pos]>lista[pos+1]:
            valor=False
        pos+=1
            
    return valor

lista = [1,2,3,4,5,6]
print(estaOrdenadaAscendemente(lista))