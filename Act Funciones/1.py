def obtieneYValidaDatosDeEntrada():
    num=-1
    while num<0:
        num=int(input("Dame un número: "))
    return num

num=obtieneYValidaDatosDeEntrada()
print(num)