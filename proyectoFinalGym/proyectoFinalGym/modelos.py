# modelos.py

class Persona:
    def __init__(self, id_persona, nombre, correo, contraseña, tipo_persona):
        self.id_persona = id_persona
        self.nombre = nombre
        self.correo = correo
        self.contraseña = contraseña
        self.tipo_persona = tipo_persona

    def iniciar_sesion(self):
        pass

    def cerrar_sesion(self):
        pass

    def actualizar(self):
        pass

class Cliente(Persona):
    def __init__(self, id_persona, nombre, correo, contraseña, tipo_persona, id_cliente, peso, estatura):
        super().__init__(id_persona, nombre, correo, contraseña, tipo_persona)
        self.id_cliente = id_cliente
        self.peso = peso
        self.estatura = estatura

    def consulta_progreso(self):
        imc = self.peso / (self.estatura ** 2)
        return f"IMC: {imc:.2f}"

class Instructor(Persona):
    def __init__(self, id_persona, nombre, correo, contraseña, tipo_persona, id_instructor, cargo, horario, sueldo):
        super().__init__(id_persona, nombre, correo, contraseña, tipo_persona)
        self.id_instructor = id_instructor
        self.cargo = cargo
        self.horario = horario
        self.sueldo = sueldo

    def instruye_cliente(self):
        pass

class Curso:
    def __init__(self, id_curso, nombre):
        self.id_curso = id_curso
        self.nombre = nombre

class Asistencia:
    def __init__(self, id_asistencia, fecha, hora_entrada, id_curso, id_cliente, id_instructor):
        self.id_asistencia = id_asistencia
        self.fecha = fecha
        self.hora_entrada = hora_entrada
       # self.hora_salida = hora_salida
        self.id_curso = id_curso
        self.id_cliente = id_cliente
        self.id_instructor = id_instructor

    def registrar_asistencia(self):
        pass

    def consultar_historial(self):
        pass
