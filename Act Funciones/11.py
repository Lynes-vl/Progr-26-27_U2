def menu():
    opciones=["S","M","H","-1"]
    option=""
    while option not in opciones:
        print("""============================
(S) Consertir a segundos
(M) Convertir a minutos
(H) Convertir a horas
(-1) Salir del programa
============================""")
        option=input().upper()
    return option

def minutos(num):
    print(f"{num//60} minutos")

def horas(num):
    print(f"{num//3600} horas")


s=(int(input("Dame los s que pasar: ")))
option=menu()
while option!="-1":
    match option:
        case "S":
            print(f"{s} segundos")
        case "M":
            minutos(s)
        case "H":
            horas(s)
    option=menu()