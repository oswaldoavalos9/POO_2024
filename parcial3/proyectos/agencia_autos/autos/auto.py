import mysql.connector
from mysql.connector import Error

class Auto:
    def __init__(self, cliente_id, marca, modelo, ano, placa):
        self.cliente_id = cliente_id
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa

    @staticmethod
    def conectar():
        """Establece la conexión con la base de datos MySQL."""
        try:
            conexion = mysql.connector.connect(
                host='localhost',    
                user='root',       
                password='',    
                database='agencia_autos'
            )
            if conexion.is_connected():
                return conexion
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            return None

    @staticmethod
    def crear_tabla():
        
        conexion = Auto.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute()
            conexion.commit()
            conexion.close()

    def registrar(self):
        """Registra un nuevo auto en la base de datos."""
        conexion = Auto.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('''INSERT INTO autos (cliente_id, marca, modelo, año, placa)
                              VALUES (%s, %s, %s, %s, %s)''',
                              (self.cliente_id, self.marca, self.modelo, self.año, self.placa))
            conexion.commit()
            conexion.close()
            return cursor.lastrowid

    @staticmethod
    def mostrar(cliente_id):
        """Muestra todos los autos registrados para un cliente específico."""
        conexion = Auto.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('''SELECT * FROM autos WHERE cliente_id = %s''', (cliente_id,))
            resultados = cursor.fetchall()
            conexion.close()
            return resultados

    @staticmethod
    def actualizar(auto_id, marca, modelo, año, placa):
        """Actualiza la información de un auto específico."""
        conexion = Auto.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('''UPDATE autos
                              SET marca = %s, modelo = %s, año = %s, placa = %s
                              WHERE id = %s''',
                              (marca, modelo, año, placa, auto_id))
            conexion.commit()
            conexion.close()
            return cursor.rowcount > 0

    @staticmethod
    def eliminar(auto_id):
        """Elimina un auto específico de la base de datos."""
        conexion = Auto.conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute('''DELETE FROM autos WHERE id = %s''', (auto_id,))
            conexion.commit()
            conexion.close()
            return cursor.rowcount > 0

# Crear la tabla de autos al ejecutar el script
if __name__ == "__main__":
    Auto.crear_tabla()