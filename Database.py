import psycopg2

# Datos de conexión
conn = psycopg2.connect(
    host="aws-0-us-east-2.pooler.supabase.com",
    port=5432,
    dbname="postgres",
    user="postgres.ehgmqnytviispgzcjolb",
    password="poo123",
    sslmode="require"  # Supabase requiere SSL
)

# Crear cursor y hacer consulta
cur = conn.cursor()
cur.execute("SELECT NOW();")
resultado = cur.fetchone()

print("Hora actual desde la base de datos:", resultado[0])

# Cerrar conexión
cur.close()
conn.close()
