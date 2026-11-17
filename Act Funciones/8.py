from math import pi

def calculaArea (radio):
    area=radio*radio*pi
    return area


def calculaPerimetro (radio):
    perimetro=2*pi*radio
    return perimetro


def calculaAreaYPerimetro(radio):
    area=radio*radio*pi
    perimetro=2*pi*radio
    return [perimetro, area]


radio= int(input("Dame el radio de la circunferencia: "))
resultado = calculaAreaYPerimetro(radio)
print(f"El área es {resultado[1]} y el perímetro {resultado[0]}")