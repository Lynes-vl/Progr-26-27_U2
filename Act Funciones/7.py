def calcularMaxMin(lista):
    maxF=lista[0]
    miniF=lista[0]
    for i in lista:
        if i > maxF:
            maxF=i
        if i < miniF:
            miniF=i
    print(f"El máximo es {maxF} y el mínimo es {miniF}")

num=[]
for i in range(1,11):
    num.append(int(input(f"Dame el {i}º número: ")))
calcularMaxMin(num)
