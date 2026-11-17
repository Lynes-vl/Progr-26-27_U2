def calculasubcadena(cadena,posI,posF):
    print("Llamo a subcadena")
    #imprimir la subcadena quedandome desde posIn hasta posFin incluida
    subcadena=cadena[posI:posF+1]
    print(subcadena)


cadena=input("Introduce una cadena con 4 caracteres: ")
while len(cadena)<4:
    x=input("Introduce una cadena con 4 caracteres: ")
#leer y validar cadena

num=int(input("Introduce un número: "))
if num%2==0:
    calculasubcadena(cadena,2,4)
elif num%3==0:
    calculasubcadena(cadena,1,2)
elif num%7==0:
    calculasubcadena(cadena,0,3)