import funtion
lista=[]
def cargarLista(lista,x):
    while 0<=x and x<=9:
        lista.append(x)
        x = int(input("Número que añadir [0-9]: "))

cargarLista(lista,int(input("Número que añadir [0-9]: ")))
print(funtion.estaOrdenadaAscendemente(lista))