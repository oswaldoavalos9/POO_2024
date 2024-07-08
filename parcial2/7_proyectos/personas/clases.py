# clase principal

class personas:
    def nombre(self):
        return self.nombre
    def edad(self):
        return self.edad
    def tel(self):
        return self.tel
    
def getnombre(self):
    return self._nombre

def getedad(self):
    return self._edad

def gettel(self):
    return self._tel

def setnombre(self, nombre):
    self.nombre = nombre

def setedad(self, edad):
    self.edad = edad

def settel(self, tel):
    self.tel = tel

def getInfo(self):
       print(f"nombre: {self.getnombre()} edad: {self.getedad()} tel: {self.gettel()}")


# clase secundaria1

class estudiantes:
    def _init_(self, carrera, matricula):
        self._carrera = carrera
        self._matricula = matricula

# metodos get y set

def getcarrera(self):
    return self._carrera

def getmatricula(self):
    return self._matricula

def setcarrera(self, carrera):
    self.carrera = carrera

def setmatricula(self, matricula):
    self.matricula = matricula

def getInfo(self):
       print(f"carrera: {self.getcarrera()} matricula: {self.getmatricula()}")
   

# # clase secundaria2
# class docentes:
#     def modalidad(self):
#         return self.modalidad
#     def num_empleado(self):
#         return self.num_empleado


