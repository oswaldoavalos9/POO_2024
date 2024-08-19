import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(user = "root", password = "",
                                           host = "localhost",
                                           database = "agencia_autos",
                                           port = "3306")
        if conexion.is_connected():
            print("conexion a la base de datos exitosa")
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
