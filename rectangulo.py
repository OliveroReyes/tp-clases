class Rectangulo:
    def __init__(self, longitud, anchura):
        self.longitud = longitud
        self.anchura = anchura

    def area(self):
        return self.longitud * self.anchura

    def perimetro(self):
        return 2 * (self.longitud + self.anchura)

rectangulo = Rectangulo(5, 3)
print(f"Área del rectángulo: {rectangulo.area()}")
print(f"Perímetro del rectángulo: {rectangulo.perimetro()}")
