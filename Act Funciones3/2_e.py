lista=[[8,1,6],[3,5,7],[4,9,2]]

def dameColumna(matriz,num):
    print(matriz[num])


num = int(input("Dame un número de columna (0-2): "))
dameColumna(lista,num)