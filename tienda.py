class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        if producto in self.productos:
            self.productos.remove(producto)

    def obtener_productos(self):
        return self.productos

tienda = Tienda("Mi Tienda")
producto1 = "Camiseta"
producto2 = "Pantalón"

tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
print(f"Productos disponibles: {tienda.obtener_productos()}")

tienda.eliminar_producto(producto1)
print(f"Productos después de eliminar {producto1}: {tienda.obtener_productos()}")
