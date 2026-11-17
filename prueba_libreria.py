def miFuncion(cadena):
    print("Estoy dentro de miFuncion: "+cadena)

def isPar(numero):
    resultado=True
    if numero %2!=0:
        resultado = False
    return resultado

def menu():
    print("""===============
Hola que hace
===============""")

def listaxd(lista):
    for i in range(3):
        lista.append(i)