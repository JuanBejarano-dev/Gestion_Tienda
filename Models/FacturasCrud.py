from Models.Facturas import Factura, DetalleFactura
from Models.ClientesCrud import ClienteCRUD
from Models.ProductosCrud import ProductoCRUD

class FacturaCRUD:
    def __init__(self):
        self.facturas = []
        self.next_id = 1
        self.clientes_crud = ClienteCRUD()
        self.productos_crud = ProductoCRUD()

    def crear(self, factura):
        factura.id = self.next_id
        self.next_id += 1
        self.facturas.append(factura)
        return factura

    def listar(self):
        return self.facturas

    def obtener_por_id(self, id):
        for factura in self.facturas:
            if factura.id == id:
                return factura
        return None

    def actualizar(self, factura_actualizada):
        for i, factura in enumerate(self.facturas):
            if factura.id == factura_actualizada.id:
                self.facturas[i] = factura_actualizada
                return True
        return False

    def eliminar(self, id):
        for i, factura in enumerate(self.facturas):
            if factura.id == id:
                del self.facturas[i]
                return True
        return False