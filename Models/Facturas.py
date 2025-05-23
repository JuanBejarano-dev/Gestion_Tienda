class Factura:
    def __init__(self, id=None, id_cliente=None, fecha=None, total=0.0, detalles=None):
        self.id = id
        self.id_cliente = id_cliente
        self.fecha = fecha
        self.total = total
        self.detalles = detalles or []
        
class DetalleFactura:
    def __init__(self, id_producto=None, cantidad=0, precio_unitario=0.0):
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario