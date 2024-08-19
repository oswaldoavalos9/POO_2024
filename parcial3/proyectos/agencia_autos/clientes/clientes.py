import mysql.connector
from mysql.connector import Error

class Cliente:
    def __init__(self, nombre, apellidos, email, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.telefono = telefono

    @staticmethod
    def conectar():
        """Establece la conexión con la base de datos MySQL."""
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='password',
                database='agencia_autos'
            )
            if conexion.is_connected():
                return conexion
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            return None

    @staticmethod
    def crear_tabla():
        """Crea la tabla de clientes si no existe."""
        conexion = Cliente.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255),
                apellidos VARCHAR(255),
                email VARCHAR(255) UNIQUE,
                telefono VARCHAR(20)
            )''')
            conexion.commit()
            conexion.close()

    def registrar(self):
        """Registra un nuevo cliente en la base de datos."""
        conexion = Cliente.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('''INSERT INTO clientes (nombre, apellidos, email, telefono)
                              VALUES (%s, %s, %s, %s)''',
                              (self.nombre, self.apellidos, self.email, self.telefono))
            conexion.commit()
            conexion.close()
            return cursor.lastrowid

    @staticmethod
    def mostrar():
        """Muestra todos los clientes registrados en la base de datos."""
        conexion = Cliente.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('''SELECT * FROM clientes''')
            resultados = cursor.fetchall()
            conexion.close()
            return resultados

    @staticmethod
    def actualizar(cliente_id, nombre, apellidos, email, telefono):
        """Actualiza la información de un cliente específico."""
        conexion = Cliente.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('''UPDATE clientes
                              SET nombre = %s, apellidos = %s, email = %s, telefono = %s
                              WHERE id = %s''',
                              (nombre, apellidos, email, telefono, cliente_id))
            conexion.commit()
            conexion.close()
            return cursor.rowcount > 0

    @staticmethod
    def eliminar(cliente_id):
        """Elimina un cliente específico de la base de datos."""
        conexion = Cliente.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('''DELETE FROM clientes WHERE id = %s''', (cliente_id,))
            conexion.commit()
            conexion.close()
            return cursor.rowcount > 0

# Crear la tabla de clientes al ejecutar el script
if __name__ == "__main__":
    Cliente.crear_tabla()