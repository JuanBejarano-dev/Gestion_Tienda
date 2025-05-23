import psycopg2
from Models.Clientes import Cliente

class ClienteCRUD:
    def __init__(self):
        self.clientes = []
        self.next_id = 1

    def crear(self, cliente):
        cliente.id = self.next_id
        self.next_id += 1
        self.clientes.append(cliente)
        return cliente

    def listar(self):
        return self.clientes

    def actualizar(self, cliente_actualizado):
        for i, cliente in enumerate(self.clientes):
            if cliente.id == cliente_actualizado.id:
                self.clientes[i] = cliente_actualizado
                return True
        return False

    def eliminar(self, id):
        for i, cliente in enumerate(self.clientes):
            if cliente.id == id:
                del self.clientes[i]
                return True
        return False