def calculaTemperaturaMedia(maxi, mini):
    media=(maxi+mini)//2
    return media

print(f"Hoy hace {calculaTemperaturaMedia(int(input("Dime la temperatura máxima de hoy: ")), int(input("Dime la temperatura mínima de hoy: ")))}º de media")
