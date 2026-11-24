import funtion
lista= [ ['a','b','c'],  ['d','e','f'], ['g','h','i']]

def imprimeMatrizInvertida(lista):
    for i in range(len(lista)):
        print(f"{lista[i]}    {lista[-i-1][::-1]}")

funtion.f1(lista)
print("---------------")
funtion.f3(lista)