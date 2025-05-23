class Producto:
    def __init__(self, id=None, nombre="", cantidad=0):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad

    def __str__(self):
        return f"[{self.id}] {self.nombre} - Cantidad: {self.cantidad}"
