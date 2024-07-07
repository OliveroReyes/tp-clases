class Libro:
    def __init__(self, titulo, autor, genero, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.num_paginas = num_paginas

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_autor(self):
        return self.autor

    def set_autor(self, autor):
        self.autor = autor

    def get_genero(self):
        return self.genero

    def set_genero(self, genero):
        self.genero = genero

    def get_num_paginas(self):
        return self.num_paginas

    def set_num_paginas(self, num_paginas):
        self.num_paginas = num_paginas

    def es_ficcion(self):
        return self.genero.lower() == "ficción"

libro = Libro("El Alquimista", "Paulo Coelho", "Novela", 200)
print(f"Título: {libro.get_titulo()}, Autor: {libro.get_autor()}, Género: {libro.get_genero()}, Número de páginas: {libro.get_num_paginas()}")

print(f"¿Es ficción?: {libro.es_ficcion()}")
