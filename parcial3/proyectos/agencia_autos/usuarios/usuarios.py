import mysql.connector
from mysql.connector import Error
import hashlib

class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = self.hash_password(password)

    @staticmethod
    def conectar():
        """Establece la conexión con la base de datos MySQL."""
        try:
            conexion = mysql.connector.connect(
                host='localhost',       # Cambia esto a la dirección de tu servidor MySQL
                user='root',            # Cambia esto a tu usuario de MySQL
                password='password',    # Cambia esto a tu contraseña de MySQL
                database='agencia_autos'  # Cambia esto al nombre de tu base de datos
            )
            if conexion.is_connected():
                return conexion
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            return None

    @staticmethod
    def crear_tabla():
        """Crea la tabla de usuarios si no existe."""
        conexion = Usuario.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255),
                apellidos VARCHAR(255),
                email VARCHAR(255) UNIQUE,
                password VARCHAR(255)
            )''')
            conexion.commit()
            conexion.close()

    @staticmethod
    def hash_password(password):
        """Genera un hash de la contraseña para almacenamiento seguro."""
        return hashlib.sha256(password.encode()).hexdigest()

    def registrar(self):
        """Registra un nuevo usuario en la base de datos."""
        conexion = Usuario.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('''INSERT INTO usuarios (nombre, apellidos, email, password)
                              VALUES (%s, %s, %s, %s)''',
                              (self.nombre, self.apellidos, self.email, self.password))
            conexion.commit()
            conexion.close()
            return cursor.lastrowid

    @staticmethod
    def iniciar_sesion(email, password):
        """Inicia sesión verificando el email y la contraseña."""
        hashed_password = Usuario.hash_password(password)
        conexion = Usuario.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('''SELECT id, nombre, apellidos FROM usuarios
                              WHERE email = %s AND password = %s''',
                              (email, hashed_password))
            resultado = cursor.fetchone()
            conexion.close()
            return resultado

    @staticmethod
    def actualizar(usuario_id, nombre, apellidos, email, password=None):
        """Actualiza la información de un usuario específico."""
        conexion = Usuario.conectar()
        if conexion:
            cursor = conexion.cursor()
            if password:
                hashed_password = Usuario.hash_password(password)
                cursor.execute('''UPDATE usuarios
                                  SET nombre = %s, apellidos = %s, email = %s, password = %s
                                  WHERE id = %s''',
                                  (nombre, apellidos, email, hashed_password, usuario_id))
            else:
                cursor.execute('''UPDATE usuarios
                                  SET nombre = %s, apellidos = %s, email = %s
                                  WHERE id = %s''',
                                  (nombre, apellidos, email, usuario_id))
            conexion.commit()
            conexion.close()
            return cursor.rowcount > 0

    @staticmethod
    def eliminar(usuario_id):
        """Elimina un usuario específico de la base de datos."""
        conexion = Usuario.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('''DELETE FROM usuarios WHERE id = %s''', (usuario_id,))
            conexion.commit()
            conexion.close()
            return cursor.rowcount > 0

# Crear la tabla de usuarios al ejecutar el script
if __name__ == "__main__":
    Usuario.crear_tabla()