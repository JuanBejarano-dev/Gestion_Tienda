import psycopg2
from Models.Productos import Producto

class ProductoCRUD:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="aws-0-us-east-2.pooler.supabase.com",
            port=5432,
            dbname="postgres",
            user="postgres.ehgmqnytviispgzcjolb",
            password="poo123",
            sslmode="require"
        )

    def crear(self, producto: Producto):
        with self.conn.cursor() as cur:
            cur.execute("INSERT INTO productos (nombre, cantidad) VALUES (%s, %s)",
                        (producto.nombre, producto.cantidad))
            self.conn.commit()

    def listar(self):
        productos = []
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, nombre, cantidad FROM productos")
            for fila in cur.fetchall():
                productos.append(Producto(id=fila[0], nombre=fila[1], cantidad=fila[2]))
        return productos

    def actualizar(self, producto: Producto):
        with self.conn.cursor() as cur:
            cur.execute("UPDATE productos SET nombre=%s, cantidad=%s WHERE id=%s",
                        (producto.nombre, producto.cantidad, producto.id))
            self.conn.commit()

    def eliminar(self, id: int):
        with self.conn.cursor() as cur:
            cur.execute("DELETE FROM productos WHERE id=%s", (id,))
            self.conn.commit()

    def actualizar_stock(self, id_producto: int, cantidad: int):
        """Actualiza el stock de un producto (suma o resta)."""
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    "UPDATE productos SET cantidad = cantidad + %s WHERE id = %s",
                    (cantidad, id_producto)
                )
                self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def cerrar(self):
        self.conn.close()
