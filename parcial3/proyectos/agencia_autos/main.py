from autos import auto
from clientes import clientes
import getpass
from funciones import *

def menu_principal():
    while True:
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Registrar Cliente
          2.- Iniciar Sesión Cliente
          3.- Salir 
          """)
        opcion = input("\t Elige una opción: ").upper()

        if opcion == '1' or opcion == "REGISTRAR CLIENTE":
            borrarPantalla()
            print("\n \t ..:: Registro de Cliente ::..")
            nombre = input("\t ¿Cuál es tu nombre?: ")
            apellidos = input("\t ¿Cuáles son tus apellidos?: ")
            email = input("\t Ingresa tu email: ")
            password = getpass.getpass("\t Ingresa tu contraseña: ")
            # Agregar código
            obj_cliente = clientes.Cliente(nombre, apellidos, email, password)
            resultado = obj_cliente.registrar()
            if resultado:
                print(f"\n\t {nombre} {apellidos}, se registró correctamente, con el email: {email}")
            else:
                print(f"\n\t ** Por favor inténtelo de nuevo, no fue posible insertar el registro ** ...")
            esperarTecla()
        elif opcion == '2' or opcion == "INICIAR SESIÓN CLIENTE":
            borrarPantalla()
            print("\n \t ..:: Inicio de Sesión Cliente ::.. ")
            email = input("\t Ingresa tu E-mail: ")
            password = getpass.getpass("\t Ingresa tu Contraseña: ")
            # Agregar código
            registro = clientes.Cliente.iniciar_sesion(email, password)
            if registro:
                menu_autos(registro[0], registro[1], registro[2])
            else:
                print(f"\n\t Email y/o contraseña incorrectos... vuelva a intentarlo ...")
                esperarTecla()
        elif opcion == '3' or opcion == "SALIR":
            print("\n\t.. ¡Gracias adios! ...")
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_autos(cliente_id, nombre, apellidos):
    while True:
        borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        print("""
                  \n \t 
                      .::  Menu Autos ::. 
                  1.- Registrar Auto
                  2.- Mostrar Autos
                  3.- Actualizar Auto
                  4.- Eliminar Auto
                  5.- Salir 
                  """)
        opcion = input("\t\t Elige una opción: ").upper()

        if opcion == '1' or opcion == "REGISTRAR AUTO":
            borrarPantalla()
            print(f"\n \t .:: Registrar Auto ::. ")
            marca = input("\tMarca: ")
            modelo = input("\tModelo: ")
            ano = input("\tAño: ")
            placa = input("\tPlaca: ")
            # Agregar código
            obj_auto = auto.Auto(cliente_id, marca, modelo, ano, placa)
            resultado = obj_auto.registrar()
            if resultado:
                print(f"\n \t \t.::El Auto {marca} {modelo} se registró correctamente ::.")
            else:
                print(f"\n \t \t** No fue posible registrar el auto ... vuelva a intentarlo **...")
            esperarTecla()
        elif opcion == '2' or opcion == "MOSTRAR AUTOS":
            borrarPantalla()
            # Agregar código
            registros = auto.Auto.mostrar(cliente_id)
            if len(registros) > 0:
                print(f"\n\t {nombre} {apellidos}, tus autos son: ")
                num_autos = 1
                for fila in registros:
                    print(f"\nAuto: {num_autos} \nID: {fila[0]}.- Marca: {fila[1]} Modelo: {fila[2]} Año: {fila[3]} Placa: {fila[4]}")
                    num_autos += 1
            else:
                print(f"\n \t \t** No existen autos para el cliente ... vuelva a intentarlo **...")
            esperarTecla()
        elif opcion == '3' or opcion == "ACTUALIZAR AUTO":
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Auto ::. \n")
            id = input("\t \t ID del auto a actualizar: ")
            marca = input("\t Nueva marca: ")
            modelo = input("\t Nuevo modelo: ")
            ano = input("\t Nuevo año: ")
            placa = input("\t Nueva placa: ")
            # Agregar código
            resultado = auto.Auto.actualizar(id, marca, modelo, ano, placa)
            if resultado:
                print(f"\n \t \t.::Auto Actualizado Correctamente ::.")
            else:
                print(f"\n \t \t** No fue posible actualizar el auto ... vuelva a intentarlo **...")
            esperarTecla()
        elif opcion == '4' or opcion == "ELIMINAR AUTO":
            borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Auto ::. \n")
            id = input("\t \t ID del auto a eliminar: ")
            # Agregar código
            resultado = auto.Auto.eliminar(id)
            if resultado:
                print(f"\n \t \t.::Auto Eliminado Correctamente ::.")
            else:
                print(f"\n \t \t** No fue posible eliminar el auto ... vuelva a intentarlo **...")
            esperarTecla()
        elif opcion == '5' or opcion == "SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

if __name__ == "__main__":
    menu_principal()