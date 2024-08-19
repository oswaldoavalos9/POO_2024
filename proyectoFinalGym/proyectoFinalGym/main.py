# main.py
import tkinter as tk
from tkinter import messagebox
from coneccionBD import conectar, crear_tablas
from modelos import Cliente, Instructor, Curso, Asistencia
from funciones import registrar_cliente, registrar_instructor, registrar_curso, registrar_asistencia#, consultar_progreso, consultar_historial_asistencias
import bcrypt
from hashlib import sha256




def registrar_cliente():
    # Crear una nueva ventana para el registro de clientes
    ventana = tk.Toplevel()
    ventana.geometry("1300x900")
    ventana.title("Registrar Cliente")

    # Función para manejar el registro cuando se presiona el botón
    def enviar_datos():
        nombre = entry_nombre.get()
        correo = entry_correo.get()
        contraseña = entry_contraseña.get()
        peso = entry_peso.get()
        estatura = entry_estatura.get()

        # Validar campos vacíos
        if not nombre or not correo or not contraseña or not peso or not estatura:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        # Validar correo
        if "@" not in correo or "." not in correo:
            messagebox.showwarning("Advertencia", "Correo no válido.")
            return

        try:
            peso = float(peso)
            estatura = float(estatura)
            if peso <= 0 or estatura <= 0:
                messagebox.showwarning("Advertencia", "Peso y estatura deben ser valores positivos.")
                return
        except ValueError:
            messagebox.showwarning("Advertencia", "Peso y estatura deben ser números.")
            return

        # Hash de la contraseña
        salt = bcrypt.gensalt()
        contraseña_hashed = bcrypt.hashpw(contraseña.encode('utf-8'), salt)

        try:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO personas (nombre, correo, contraseña, tipo_persona) VALUES (%s, %s, %s, %s)",
                (nombre, correo, contraseña_hashed, 'cliente')
            )
            
            id_persona = cursor.lastrowid
            cursor.execute(
                "INSERT INTO clientes (id_persona, peso, estatura) VALUES (%s, %s, %s)",
                (id_persona, peso, estatura)
            )
            conexion.commit()
            messagebox.showinfo("Éxito", "Cliente registrado exitosamente.")
            ventana.destroy()
        
        except Exception as e:
            conexion.rollback()
            messagebox.showerror("Error", f"Error al registrar cliente: {e}")

    # Etiquetas y campos de entrada
    tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Correo:").grid(row=1, column=0, padx=10, pady=5)
    entry_correo = tk.Entry(ventana)
    entry_correo.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Contraseña:").grid(row=2, column=0, padx=10, pady=5)
    entry_contraseña = tk.Entry(ventana, show="*")
    entry_contraseña.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Peso (kg):").grid(row=3, column=0, padx=10, pady=5)
    entry_peso = tk.Entry(ventana)
    entry_peso.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Estatura (m):").grid(row=4, column=0, padx=10, pady=5)
    entry_estatura = tk.Entry(ventana)
    entry_estatura.grid(row=4, column=1, padx=10, pady=5)

    # Botón para registrar cliente
    boton_registrar = tk.Button(ventana, text="Registrar", command=enviar_datos)
    boton_registrar.grid(row=5, columnspan=2, pady=10)

    boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
    boton_salir.grid(row=6, columnspan=2, pady=5)

    ventana.mainloop()
    

def registrar_instructor():
    # Crear una nueva ventana para el registro de instructores
    ventana = tk.Toplevel()
    ventana.geometry("400x300")
    ventana.title("Registrar Instructor")

    # Función para manejar el registro cuando se presiona el botón
    def enviar_datos():
        id_instructor = entry_id_instructor.get()
        id_persona = entry_id_persona.get()
        horario = entry_horario.get()
        sueldo = entry_sueldo.get()

        # Validar campos vacíos
        if not id_instructor or not id_persona or not horario or not sueldo:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        try:
            sueldo = float(sueldo)
            if sueldo <= 0:
                messagebox.showwarning("Advertencia", "El sueldo debe ser un valor positivo.")
                return
        except ValueError:
            messagebox.showwarning("Advertencia", "El sueldo debe ser un número.")
            return

        # Verificar si id_persona existe en la tabla personas
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id_persona FROM personas WHERE id_persona = %s", (id_persona,))
            if cursor.fetchone() is None:
                messagebox.showwarning("Advertencia", "El ID de persona proporcionado no existe.")
                return

            # Insertar en la tabla instructores
            cursor.execute("INSERT INTO instructores (id_instructor, id_persona, horario, sueldo) VALUES (%s, %s, %s, %s)",
                           (id_instructor, id_persona, horario, sueldo))
            
            conexion.commit()
            messagebox.showinfo("Éxito", f"Instructor registrado exitosamente con ID {id_instructor}.")
            ventana.destroy()
        
        except Exception as e:
            conexion.rollback()
            messagebox.showerror("Error", f"Error al registrar instructor: {e}")

    # Etiquetas y campos de entrada
    tk.Label(ventana, text="ID Instructor:").grid(row=0, column=0, padx=10, pady=5)
    entry_id_instructor = tk.Entry(ventana)
    entry_id_instructor.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(ventana, text="ID Persona:").grid(row=1, column=0, padx=10, pady=5)
    entry_id_persona = tk.Entry(ventana)
    entry_id_persona.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Horario:").grid(row=2, column=0, padx=10, pady=5)
    entry_horario = tk.Entry(ventana)
    entry_horario.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Sueldo:").grid(row=3, column=0, padx=10, pady=5)
    entry_sueldo = tk.Entry(ventana)
    entry_sueldo.grid(row=3, column=1, padx=10, pady=5)

    # Botón para registrar instructor
    boton_registrar = tk.Button(ventana, text="Registrar", command=lambda: enviar_datos())
    boton_registrar.grid(row=4, columnspan=2, pady=10)

    boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
    boton_salir.grid(row=5, columnspan=2, pady=5)

    ventana.mainloop()

def registrar_curso():
    # Crear una nueva ventana para el registro de cursos
    ventana = tk.Toplevel()
    ventana.geometry("600x300")
    ventana.title("Registrar Curso")

    # Función para manejar el registro cuando se presiona el botón
    def enviar_datos():
        id_curso = entry_id_curso.get()
        nombre = entry_nombre.get()

        # Validar campos vacíos
        if not id_curso or not nombre:
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        try:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO cursos (id_curso, nombre) VALUES (%s, %s)",
                (id_curso, nombre)
            )
            conexion.commit()
            messagebox.showinfo("Éxito", "Curso registrado exitosamente.")
            ventana.destroy()

        except Exception as e:
            conexion.rollback()
            messagebox.showerror("Error", f"Error al registrar curso: {e}")

    # Etiquetas y campos de entrada
    tk.Label(ventana, text="ID Curso:").grid(row=0, column=0, padx=10, pady=5)
    entry_id_curso = tk.Entry(ventana)
    entry_id_curso.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Nombre:").grid(row=1, column=0, padx=10, pady=5)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=1, column=1, padx=10, pady=5)

    # Botón para registrar curso
    boton_registrar = tk.Button(ventana, text="Registrar", command=enviar_datos)
    boton_registrar.grid(row=2, columnspan=2, pady=10)

    # Botón para salir
    boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
    boton_salir.grid(row=3, columnspan=2, pady=5)

    ventana.mainloop()

    

def registrar_asistencia():
    # Crear una nueva ventana para el registro de asistencias
    ventana = tk.Toplevel()
    ventana.geometry("800x500")
    ventana.title("Registrar Asistencia")

    # Función para manejar el registro cuando se presiona el botón
    def enviar_datos():
        id_asistencia = entry_id_asistencia.get()
        fecha = entry_fecha.get()
        hora_entrada = entry_hora_entrada.get()
        id_curso = entry_id_curso.get()
        id_cliente = entry_id_cliente.get()
        id_instructor = entry_id_instructor.get()
        #hora_salida = entry_hora_salida.get()

        # Validar campos vacíos
        if not id_asistencia or not fecha or not hora_entrada or not id_curso or not id_cliente or not id_instructor: #or not, hora_salida
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios.")
            return

        try:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO asistencias (id_asistencia, fecha, hora_entrada, id_curso, id_cliente, id_instructor) VALUES (%s, %s, %s, %s, %s, %s)",
                (id_asistencia, fecha, hora_entrada, id_curso, id_cliente, id_instructor) #hora_salida)
            )
            conexion.commit()
            messagebox.showinfo("Éxito", "Asistencia registrada exitosamente.")
            ventana.destroy()

        except Exception as e:
            conexion.rollback()
            messagebox.showerror("Error", f"Error al registrar asistencia: {e}")

    # Etiquetas y campos de entrada
    tk.Label(ventana, text="ID Asistencia:").grid(row=0, column=0, padx=10, pady=5)
    entry_id_asistencia = tk.Entry(ventana)
    entry_id_asistencia.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Fecha (YYYY-MM-DD):").grid(row=4, column=0, padx=10, pady=5)
    entry_fecha = tk.Entry(ventana)
    entry_fecha.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Hora de Entrada (HH:MM):").grid(row=5, column=0, padx=10, pady=5)
    entry_hora_entrada = tk.Entry(ventana)
    entry_hora_entrada.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(ventana, text="ID Curso:").grid(row=3, column=0, padx=10, pady=5)
    entry_id_curso = tk.Entry(ventana)
    entry_id_curso.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(ventana, text="ID Cliente:").grid(row=1, column=0, padx=10, pady=5)
    entry_id_cliente = tk.Entry(ventana)
    entry_id_cliente.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana, text="ID Instructor:").grid(row=2, column=0, padx=10, pady=5)
    entry_id_instructor = tk.Entry(ventana)
    entry_id_instructor.grid(row=2, column=1, padx=10, pady=5)

    #tk.Label(ventana, text="Hora de Salida (HH:MM):").grid(row=6, column=0, padx=10, pady=5)
    #entry_hora_salida = tk.Entry(ventana)
    #entry_hora_salida.grid(row=6, column=1, padx=10, pady=5)

    # Botón para registrar asistencia
    boton_registrar = tk.Button(ventana, text="Registrar", command=enviar_datos)
    boton_registrar.grid(row=7, columnspan=2, pady=10)

    # Botón para salir
    boton_salir = tk.Button(ventana, text="Salir", command=ventana.destroy)
    boton_salir.grid(row=8, columnspan=2, pady=5)

    ventana.mainloop()







def mostrar_menu():
    ventana = tk.Tk()
    ventana.geometry("1300x900") 
    ventana.title("Sistema de Monitoreo de GYM")

    # Título principal
    titulo = tk.Label(ventana, text="Sistema de Monitoreo de GYM", font=("Helvetica", 24, "bold"))
    titulo.grid(row=0, column=0, columnspan=2, pady=20)

    # Botones
    boton_registrar = tk.Button(ventana, text="Registrar Cliente", font=("Helvetica", 14), command=registrar_cliente)
    boton_registrar.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    boton_registrar_instructor = tk.Button(ventana, text="Registrar Instructor", font=("Helvetica", 14), command=registrar_instructor)
    boton_registrar_instructor.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    boton_registrar_curso = tk.Button(ventana, text="Registrar Curso", font=("Helvetica", 14), command=registrar_curso)
    boton_registrar_curso.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    boton_registrar_asistencia = tk.Button(ventana, text="Registrar Asistencia", font=("Helvetica", 14), command=registrar_asistencia)
    boton_registrar_asistencia.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    boton_quit_menu = tk.Button(ventana, text="Salir del menú", font=("Helvetica", 14), command=ventana.quit)
    boton_quit_menu.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    # Hacer que las columnas se expandan uniformemente
    ventana.grid_columnconfigure(0, weight=1)
    ventana.grid_columnconfigure(1, weight=1)

    ventana.mainloop()




if __name__ == "__main__":
    conexion = conectar()
    crear_tablas()
    mostrar_menu()




