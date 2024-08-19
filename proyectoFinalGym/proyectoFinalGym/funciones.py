# gym/funciones.py

from modelos import *

def registrar_cliente(conexion):
    nombre = input("Ingrese el nombre del cliente: ")
    correo = input("Ingrese el correo del cliente: ")
    contraseña = input("Ingrese la contraseña del cliente: ")
    peso = float(input("Ingrese el peso del cliente: "))
    estatura = float(input("Ingrese la estatura del cliente: "))

    cursor = conexion.cursor()
    cursor.execute("INSERT INTO personas (nombre, correo, contraseña, tipo_persona) VALUES (%s, %s, %s, %s)",
                   (nombre, correo, contraseña, 'cliente'))
    
    id_persona = cursor.lastrowid
    cursor.execute("INSERT INTO clientes (id_persona, peso, estatura) VALUES (%s, %s, %s)",
                   (id_persona, peso, estatura))
    conexion.commit()
    print("Cliente registrado exitosamente.")

def registrar_instructor(conexion):
    id_instructor = input("Ingrese el ID del instructor: ")
    id_persona = input("Ingrese el ID de la persona asociado: ")
    horario = input("Ingrese el horario del instructor: ")
    sueldo = float(input("Ingrese el sueldo del instructor: "))

    cursor = conexion.cursor()

    try:
        # Verificar si id_persona existe en la tabla personas
        cursor.execute("SELECT id_persona FROM personas WHERE id_persona = %s", (id_persona,))
        if cursor.fetchone() is None:
            print("Error: El ID de persona proporcionado no existe.")
            return

        # Insertar en la tabla instructores
        cursor.execute("INSERT INTO instructores (id_instructor, id_persona, horario, sueldo) VALUES (%s, %s, %s, %s)",
                       (id_instructor, id_persona, horario, sueldo))
        
        conexion.commit()
        print(f"Instructor registrado exitosamente con ID {id_instructor}.")
    
    except Exception as e:
        conexion.rollback()
        print(f"Error al registrar instructor: {e}")


def registrar_curso(conexion):
    nombre = input("Ingrese el nombre del curso: ")

    cursor = conexion.cursor()
    cursor.execute("INSERT INTO cursos (nombre) VALUES (%s)", (nombre,))
    conexion.commit()
    print("Curso registrado exitosamente.")

def registrar_asistencia(conexion):
    fecha = input("Ingrese la fecha de la asistencia (YYYY-MM-DD): ")
    hora_entrada = input("Ingrese la hora de entrada (HH:MM:SS): ")
    #hora_salida = input("Ingrese la hora de salida (HH:MM:SS): ")
    id_curso = int(input("Ingrese el ID del curso: "))
    id_cliente = int(input("Ingrese el ID del cliente: "))
    id_instructor = int(input("Ingrese el ID del instructor: "))

    cursor = conexion.cursor()
    cursor.execute("INSERT INTO asistencias (fecha, hora_entrada, id_curso, id_cliente, id_instructor) VALUES (%s, %s, %s, %s, %s)",
                   (fecha, hora_entrada, id_curso, id_cliente, id_instructor))
    conexion.commit()
    print("Asistencia registrada exitosamente.")

#def consultar_progreso(conexion):
   # id_cliente = int(input("Ingrese el ID del cliente: "))

    #cursor = conexion.cursor()
    #cursor.execute("SELECT peso, estatura FROM clientes WHERE id_persona = %s", (id_cliente,))
    #resultado = cursor.fetchone()
    #if resultado:
     #   peso, estatura = resultado
      #  imc = peso / (estatura ** 2)
       # print(f"Peso: {peso}, Estatura: {estatura}, IMC: {imc:.2f}")
    #else:
     #   print("Cliente no encontrado.")

#def consultar_historial_asistencias(conexion, id_cliente):
   # cursor = conexion.cursor()
   # cursor.execute("SELECT fecha, hora_entrada, hora_salida FROM asistencias WHERE id_cliente = %s", (id_cliente,))
   # asistencias = cursor.fetchall()
   # return asistencias
