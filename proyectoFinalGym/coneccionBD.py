# coneccionBD.py
import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gym"
    )
    return conexion

def crear_tablas():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS personas (
        id_persona INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100),
        correo VARCHAR(100),
        contraseña VARCHAR(100),
        tipo_persona VARCHAR(50)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id_cliente INT AUTO_INCREMENT PRIMARY KEY,
        id_persona INT,
        peso FLOAT,
        estatura FLOAT,
        FOREIGN KEY (id_persona) REFERENCES personas(id_persona)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS instructores (
        id_instructor INT AUTO_INCREMENT PRIMARY KEY,
        id_persona INT,
        cargo VARCHAR(100),
        horario VARCHAR(50),
        sueldo FLOAT,
        FOREIGN KEY (id_persona) REFERENCES personas(id_persona)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cursos (
        id_curso INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS asistencias (
        id_asistencia INT AUTO_INCREMENT PRIMARY KEY,
        fecha DATE,
        hora_entrada TIME,
        hora_salida TIME,
        id_curso INT,
        id_cliente INT,
        id_instructor INT,
        FOREIGN KEY (id_curso) REFERENCES cursos(id_curso),
        FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
        FOREIGN KEY (id_instructor) REFERENCES instructores(id_instructor)
    )""")
    
    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    crear_tablas()


