class Coche:
    def __init__(self, marca, modelo, año_fabricacion):
        self.marca = marca
        self.modelo = modelo
        self.año_fabricacion = año_fabricacion

    def años_desde_fabricacion(self, año_actual):
        return año_actual - self.año_fabricacion

coche = Coche("Toyota", "Corolla", 2019)
print(f"Años desde la fabricación: {coche.años_desde_fabricacion(2024)} años")
