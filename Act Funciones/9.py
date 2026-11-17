def Login(nom,contr):
    resultado=False
    if nom=="usuario1":
        if contr=="asdasd":
            resultado=True
    return resultado

login=True
intentos=0
while intentos<3 and login:
    if Login(input("Introduce el usuario: "),input("Introduce la contraseña: ")):
        login=False
    else:
        print("Error")
        intentos+=1
if intentos==3:
    print("Intentos agotaddos")
else:
    print("Login completado")