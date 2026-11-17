def calculaMayoresQueNumero(lista,numero):
    for i in range(5):
        numero+=1
        lista.append(numero)

x=[]
calculaMayoresQueNumero(x,int(input("Dame un número: ")))
print(x)
