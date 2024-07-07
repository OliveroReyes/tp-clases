class Banco:
    def __init__(self, nombre, tasa_interes):
        self.nombre = nombre
        self.tasa_interes = tasa_interes

    def calcular_interes(self, cantidad, tiempo):
        return cantidad * ((1 + self.tasa_interes) ** tiempo - 1)

    def tiempo_para_duplicar(self):
        return 72 / (self.tasa_interes * 100)

banco = Banco("Mi Banco", 0.05)
print(f"Interés después de 5 años para $1000: ${banco.calcular_interes(1000, 5):.2f}")
print(f"Años para duplicar la inversión: {banco.tiempo_para_duplicar():.2f} años")
