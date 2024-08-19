import mysql.connector
from mysql.connector import Error


def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            port='3306',
            database='mi_empresa',
            user='root',
            password=''
        )
        if conexion.is_connected():
           # print("Conexión a la base de datos establecida.")
            return conexion
    except Error as e:
        #print(f"Error al conectar a la base de datos: {e}")
        return None

def cerrar_conexion(conexion):
    if conexion and conexion.is_connected():
        conexion.close()
        #print("Conexión cerrada correctamente.")