class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def aumentar_stock(self, cantidad):
        self.stock += cantidad

    def disminuir_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
        else:
            print("No hay suficiente stock")

producto = Producto("Laptop", 1200, 10)
print(f"Producto: {producto.nombre}, Precio: ${producto.precio}, Stock: {producto.stock}")

producto.aumentar_stock(5)
print(f"Nuevo stock: {producto.stock}")

producto.disminuir_stock(3)
print(f"Stock actualizado: {producto.stock}")
