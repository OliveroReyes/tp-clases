class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.notas = []

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_carrera(self):
        return self.carrera

    def set_carrera(self, carrera):
        self.carrera = carrera

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_nota_media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0

estudiante = Estudiante("Ana", 20, "Informática")
print(f"Nombre: {estudiante.get_nombre()}, Edad: {estudiante.get_edad()}, Carrera: {estudiante.get_carrera()}")

# Agregar notas y calcular la nota media
estudiante.agregar_nota(80)
estudiante.agregar_nota(75)
estudiante.agregar_nota(90)
print(f"Nota media: {estudiante.calcular_nota_media()}")
