class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def asistencia(self):
        print(f"{self.nombre} {self.apellido} está presente.")

class PersonalLimpieza(Persona):
    def __init__(self, nombre, apellido, edad, id_PL, horario, sueldo):
        super().__init__(nombre, apellido, edad)
        self.id_PL = id_PL
        self.horario = horario
        self.sueldo = sueldo

    def limpia(self):
        print(f"{self.nombre} {self.apellido} está limpiando.")

class Cliente(Persona):
    def __init__(self, nombre, apellido, edad, id_cliente, peso, estatura):
        super().__init__(nombre, apellido, edad)
        self.id_cliente = id_cliente
        self.peso = peso
        self.estatura = estatura

    def entrena(self):
        print(f"{self.nombre} {self.apellido} está entrenando.")

class Instructor(Persona):
    def __init__(self, nombre, apellido, edad, id_instructor, horario, sueldo):
        super().__init__(nombre, apellido, edad)
        self.id_instructor = id_instructor
        self.horario = horario
        self.sueldo = sueldo

    def orienta(self):
        print(f"{self.nombre} {self.apellido} está orientando a los clientes.")
   