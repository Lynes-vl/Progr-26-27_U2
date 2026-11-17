def calcularMax(num):
    maxi=num[0]
    for i in num:
        if i>maxi:
            maxi=i
    return maxi

numeros=[]
print("Dame 10 números")
for i in range(1,11):
    numeros.append(int(input(f"número {i}: ")))
print(f"El máximo es el número {calcularMax(numeros)}")