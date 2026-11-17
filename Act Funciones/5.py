def ConvertirEspaciado(texto):
    resultado=""
    for i in texto:
        if i != " ":
            resultado=resultado+i+" "
    return resultado

print(ConvertirEspaciado(input("Dame un texto: ")))