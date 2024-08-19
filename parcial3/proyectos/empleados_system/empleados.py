from conexionBD import crear_conexion

class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def crear(self):
        conexion = crear_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute(
                    "INSERT INTO empleados (nombre, puesto, salario) VALUES (%s, %s, %s)",
                    (self.nombre, self.puesto, self.salario)
                )
                conexion.commit()
                print("Empleado creado exitosamente.")
                return True
            except Exception as e:
                print(f"Error al crear el empleado: {e}")
                return False
           # finally:
                #cerrar_conexion(conexion)

    @staticmethod
    def mostrar():
        conexion = crear_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM empleados")
                resultados = cursor.fetchall()
                return resultados
            except Exception as e:
                print(f"Error al leer los empleados: {e}")
                return []
            #finally:
                #cerrar_conexion(conexion)

    @staticmethod
    def actualizar(id, nombre, puesto, salario):
        conexion = crear_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute(
                    "UPDATE empleados SET nombre = %s, puesto = %s, salario = %s WHERE id = %s",
                    (nombre, puesto, salario, id)
                )
                conexion.commit()
                print("Empleado actualizado exitosamente.")
                return True
            except Exception as e:
                print(f"Error al actualizar el empleado: {e}")
                return False
            #finally:
               # cerrar_conexion(conexion)

    @staticmethod
    def eliminar(id):
        conexion = crear_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute(
                    "DELETE FROM empleados WHERE id = %s",
                    (id,)
                )
                conexion.commit()
                print("Empleado eliminado exitosamente.")
                return True
            except Exception as e:
                print(f"Error al eliminar el empleado: {e}")
                return False
            #finally:
                #cerrar_conexion(conexion)