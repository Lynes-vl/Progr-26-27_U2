def esMultiplo(n1,n2):
    valido=False
    if n1%n2==0:
        valido=True
    return valido

n1=int(input("Dame un número: "))
n2=int(input("Dame otro número: "))
print(esMultiplo(n1,n1))