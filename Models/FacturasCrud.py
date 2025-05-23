import psycopg2
from Models.Facturas import Factura, DetalleFactura

class FacturaCRUD:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="aws-0-us-east-2.pooler.supabase.com",
            port=5432,
            dbname="postgres",
            user="postgres.ehgmqnytviispgzcjolb",
            password="poo123",
            sslmode="require"
        )
        self.conn.autocommit = False  # Manejar transacciones manualmente

    def crear(self, factura: Factura):
        try:
            with self.conn.cursor() as cur:
                # Insertar factura y obtener el ID generado
                cur.execute(
                    """INSERT INTO facturas (id_cliente, fecha, total)
                       VALUES (%s, %s, %s) RETURNING id""",
                    (factura.id_cliente, factura.fecha, factura.total)
                )
                factura_id = cur.fetchone()[0]
                
                # Insertar detalles (corregido: usar crear_detalle)
                for detalle in factura.detalles:
                    self.crear_detalle(cur, factura_id, detalle)
                
                self.conn.commit()
                return factura_id
        except Exception as e:
            self.conn.rollback()
            raise e

    def crear_detalle(self, cursor, factura_id: int, detalle: DetalleFactura):
        cursor.execute(
            """INSERT INTO detalle_facturas 
               (id_factura, id_producto, cantidad, precio_unitario)
               VALUES (%s, %s, %s, %s)""",
            (factura_id, detalle.id_producto, detalle.cantidad, detalle.precio_unitario)
        )

    def listar(self):
        facturas = []
        with self.conn.cursor() as cur:
            cur.execute("SELECT id, id_cliente, fecha, total FROM facturas")
            for fila in cur.fetchall():
                factura = Factura(*fila)
                factura.detalles = self.obtener_detalles(cur, factura.id)
                facturas.append(factura)
        return facturas

    def obtener_detalles(self, cursor, factura_id: int):
        cursor.execute(
            "SELECT id_producto, cantidad, precio_unitario FROM detalle_facturas WHERE id_factura = %s",
            (factura_id,)
        )
        return [DetalleFactura(*det) for det in cursor.fetchall()]

    def eliminar(self, factura_id: int):
        try:
            with self.conn.cursor() as cur:
                # Eliminar detalles primero
                cur.execute("DELETE FROM detalle_facturas WHERE id_factura = %s", (factura_id,))
                # Eliminar factura
                cur.execute("DELETE FROM facturas WHERE id = %s", (factura_id,))
                self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            if exc_type is None:
                self.conn.commit()
            else:
                self.conn.rollback()
            self.cerrar()

    def cerrar(self):
        if self.conn and not self.conn.closed:
            self.conn.close()