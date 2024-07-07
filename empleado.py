class Empleado:
    def __init__(self, nombre, edad, salario, cargo):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.cargo = cargo

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_salario(self):
        return self.salario

    def set_salario(self, salario):
        self.salario = salario

    def get_cargo(self):
        return self.cargo

    def set_cargo(self, cargo):
        self.cargo = cargo

    def calcular_salario_anual(self):
        return self.salario * 12

empleado = Empleado("Carlos", 30, 2500, "Desarrollador")
print(f"Nombre: {empleado.get_nombre()}, Edad: {empleado.get_edad()}, Cargo: {empleado.get_cargo()}")


empleado.set_salario(3000)
print(f"Salario anual: ${empleado.calcular_salario_anual()}")
