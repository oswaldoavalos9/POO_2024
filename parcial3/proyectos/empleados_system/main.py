from empleados import Empleado
from funciones import limpiar_pantalla, esperar_tecla

def crear_empleado():
    limpiar_pantalla()
    nombre = input("Nombre: ")
    puesto = input("Puesto: ")
    salario = input("Salario: ")
    empleado = Empleado(nombre, puesto,  salario)
    empleado.crear()
    esperar_tecla()

def leer_empleados():
    limpiar_pantalla()
    empleados = Empleado.mostrar()
    if empleados:
        for fila in empleados:
            print(f"ID: {fila[0]}, Nombre: {fila[1]}, Puesto: {fila[2]}, Salario: {fila[3]}")
    else:
        print("No se encontraron empleados.")
    esperar_tecla()

def actualizar_empleado():
    limpiar_pantalla()
    id = input("ID del empleado a actualizar: ")
    nombre = input("Nuevo nombre: ")
    puesto = input("Nuevo puesto: ")
    salario = input("Nuevo salario: ")
    Empleado.actualizar(id, nombre, puesto, salario)
    esperar_tecla()

def eliminar_empleado():
    limpiar_pantalla()
    id = input("ID del empleado a eliminar: ")
    Empleado.eliminar(id)
    esperar_tecla()

def menu():
    while True:
        limpiar_pantalla()
        print("\n--- ..:: Menú de Opciones ::.. ---")
        print("1. Crear empleado")
        print("2. Leer empleados")
        print("3. Actualizar empleado")
        print("4. Eliminar empleado")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            crear_empleado()
        elif opcion == '2':
            leer_empleados()
        elif opcion == '3':
            actualizar_empleado()
        elif opcion == '4':
            eliminar_empleado()
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
            esperar_tecla()

if __name__ == "__main__":
    menu()