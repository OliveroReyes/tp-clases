class Persona:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura

persona = Persona("Juan", 30, 1.75)
print(f"Nombre: {persona.get_nombre()}, Edad: {persona.get_edad()}, Altura: {persona.get_altura()}")

persona.set_nombre("María")
persona.set_edad(28)
persona.set_altura(1.70)

print(f"Nombre: {persona.get_nombre()}, Edad: {persona.get_edad()}, Altura: {persona.get_altura()}")

