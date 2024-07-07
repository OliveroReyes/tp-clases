import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.diametro = 2 * radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def circunferencia(self):
        return 2 * math.pi * self.radio

circulo = Circulo(5)
print(f"Área del círculo: {circulo.area()}")
print(f"Circunferencia del círculo: {circulo.circunferencia()}")
