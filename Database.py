import sqlite3 

try: 
    conexion = sqlite3.connect("bd_Tienda")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE Persona (nombre VARCHAR(50))")
except Exception as ex:
    print("Error al conectar a la base de datos: ", ex)