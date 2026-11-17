def calculaTemperaturaMedia(maxi, mini):
    media=(maxi+mini)//2
    return media

num=int(input("Dime el número de días para los que se desea calcular la temperatura media: "))
for i in range(1, num+1):
    print(f"La temperatura media del día {i} es de {calculaTemperaturaMedia(int(input(f"Dime la temperatura máxima del día {i}: ")), int(input(f"Dime la temperatura mínima del día {i}: ")))}º")