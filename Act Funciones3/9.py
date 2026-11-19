import random
num=[]
bucle=True
for i in range(100):
    num.append(random.randint(0,100))

def menu():
    print("""===================================================================================
(A) Conocer el mayor    
(B) Conocer el menor
(C) Obtener la suma de todos los números
(D) Obtener la media
(E) Sustituir el valor de un elemento por otro número introducido por teclado
(F) Mostrar todos los números
Elige una opción
===================================================================================""")
    return input().upper()

def mayor(num):
    x=num[0]
    for i in num:
        if i>x:
            x=i
    return x

def menor(num):
    x=num[0]
    for i in num:
        if i<x:
            x=i
    return x

def suma(num):
    x=0
    for i in num:
        x+=i
    return x

def media(num):
    x=suma(num)
    x=x//100
    return x

def reemplazar(num):
    pos=random.randint(0,99)
    x=int(input(f"Sustituye el número {num[pos]} por: "))
    num[pos]=x
while bucle:
    option=menu()
    match option:
        case "A":
            print(f"El número mayor es {mayor(num)}.")
        case "B":
            print(f"El número menor es {menor(num)}.")
        case "C":
            print(f"La suma de todos los números es {suma(num)}.")
        case "D":
            print(f"La media es {media(num)}.")
        case "E":
            reemplazar(num)
        case "F":
            print(num)