import mysql.connector
from mysql.connector import Error

class Revision:
    def __init__(self, auto_id, fecha, tipo_mantenimiento, kilometraje, nota):
        self.auto_id = auto_id
        self.fecha = fecha
        self.tipo_mantenimiento = tipo_mantenimiento
        self.kilometraje = kilometraje
        self.nota = nota

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
        """Crea la tabla de revisiones si no existe."""
        conexion = Revision.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS revisiones (
                id INT AUTO_INCREMENT PRIMARY KEY,
                auto_id INT,
                fecha DATE,
                tipo_mantenimiento VARCHAR(255),
                kilometraje INT,
                nota TEXT,
                FOREIGN KEY(auto_id) REFERENCES autos(id)
            )''')
            conexion.commit()
            conexion.close()

    def registrar(self):
        """Registra una nueva revisión en la base de datos."""
        conexion = Revision.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('''INSERT INTO revisiones (auto_id, fecha, tipo_mantenimiento, kilometraje, nota)
                              VALUES (%s, %s, %s, %s, %s)''',
                              (self.auto_id, self.fecha, self.tipo_mantenimiento, self.kilometraje, self.nota))
            conexion.commit()
            conexion.close()
            return cursor.lastrowid

    @staticmethod
    def mostrar(auto_id):
        """Muestra todas las revisiones registradas para un auto específico."""
        conexion = Revision.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('''SELECT * FROM revisiones WHERE auto_id = %s''', (auto_id,))
            resultados = cursor.fetchall()
            conexion.close()
            return resultados

    @staticmethod
    def actualizar(revision_id, fecha, tipo_mantenimiento, kilometraje, nota):
        """Actualiza la información de una revisión específica."""
        conexion = Revision.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('''UPDATE revisiones
                              SET fecha = %s, tipo_mantenimiento = %s, kilometraje = %s, nota = %s
                              WHERE id = %s''',
                              (fecha, tipo_mantenimiento, kilometraje, nota, revision_id))
            conexion.commit()
            conexion.close()
            return cursor.rowcount > 0

    @staticmethod
    def eliminar(revision_id):
        """Elimina una revisión específica de la base de datos."""
        conexion = Revision.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('''DELETE FROM revisiones WHERE id = %s''', (revision_id,))
            conexion.commit()
            conexion.close()
            return cursor.rowcount > 0

# Crear la tabla de revisiones al ejecutar el script
if __name__ == "__main__":
    Revision.crear_tabla()