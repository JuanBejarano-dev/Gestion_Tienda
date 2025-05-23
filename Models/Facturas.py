class Factura:
    def __init__(self, id: int, id_cliente: int, fecha: str, total: float):
        self.id = id
        self.id_cliente = id_cliente
        self.fecha = fecha
        self.total = total
        self.detalles = []  # Lista de objetos DetalleFactura

class DetalleFactura:
    def __init__(self, id_producto: int, cantidad: int, precio_unitario: float):
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario