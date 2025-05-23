import psycopg2
from Models.Clientes import Cliente

class ClienteCRUD:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="aws-0-us-east-2.pooler.supabase.com",
            port=5432,
            dbname="postgres",
            user="postgres.ehgmqnytviispgzcjolb",
            password="poo123",
            sslmode="require"
        )

    def crear(self, cliente: Cliente):
        with self.conn.cursor() as cur:
            cur.execute(
                "INSERT INTO clientes (nombre, apellido, correo) VALUES (%s, %s, %s)",
                (cliente.nombre, cliente.apellido, cliente.correo)
            )
            self.conn.commit()

    def listar(self):
        clientes = []
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, nombre, apellido, correo FROM clientes")
            for fila in cur.fetchall():
                clientes.append(Cliente(id=fila[0], nombre=fila[1], apellido=fila[2], correo=fila[3]))
        return clientes

    def actualizar(self, cliente: Cliente):
        with self.conn.cursor() as cur:
            cur.execute(
                "UPDATE clientes SET nombre=%s, apellido=%s, correo=%s WHERE id=%s",
                (cliente.nombre, cliente.apellido, cliente.correo, cliente.id)
            )
            self.conn.commit()

    def eliminar(self, id: int):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM clientes WHERE id=%s", (id,))
            self.conn.commit()

    def cerrar(self):
        self.conn.close()