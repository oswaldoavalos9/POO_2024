# clase padre
class lectores:
    def __init__(self,nombre, direccion, tel):
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel
        
    def reservar(self):
        print(f"El docente: {self.getNombre()} reservo un libro y su numero de empleado es: {self.getNum_empleado()} de la modalidad de: {self.getModalidad()}")

    def entregar(self):
        print(f"El docente: {self.getNombre()} entrego un libro y su numero de empleado es: {self.getNum_empleado()} de la modalidad de: {self.getModalidad()}")

# get y set

    def getnombre(self):
        return self.nombre
    
    def getdireccion(self):
        return self.direccion
        
    def gettel(self):
        return self.tel    
    
    def setnombre(self, nombre):
        self.nombre = nombre

    def setdireccion(self, direccion):
        self.direccion = direccion

    def settel(self, tel):
        self.tel = tel    


# clase secundaria
class estudiantes(lectores):
    def __init__(self, nombre, direccion, tel, carrera, matricula):
        super().__init__(nombre, direccion, tel)
        self._carrera = carrera
        self._matricula = matricula

    def reservar(self):
        print(f"El estudiante: {self.getNombre()} reservo un libro y su matricula es: {self.getMatricula()} de la carrera de: {self.getCarrera()}")

    def entregar(self):
        print(f"El estudiante: {self.getNombre()} entrego un libro y su matricula es: {self.getMatricula()} de la carrera de: {self.getCarrera()}")
# get y set

    def getcarrera(self):
        return self.carrera
    
    def getmatricula(self):
        return self.matricula
        
    
    def setnombre(self, carrera):
        self.carrera = carrera

    def setmatricula(self, matricula):
        self.matricula = matricula


# clase secundaria
class docentes(lectores):
    def __init__(self, nombre, direccion, tel, modalidad, num_empleado):
        super().__init__(nombre, direccion, tel)
        self._modalidad = modalidad
        self._num_empleado = num_empleado

    def reservar(self):
        print(f"El docente: {self.getNombre()} reservo un libro y su numero de empleado es: {self.getNum_empleado()} de la modalidad de: {self.getModalidad()}")

    def entregar(self):
        print(f"El docente: {self.getNombre()} entrego un libro y su numero de empleado es: {self.getNum_empleado()} de la modalidad de: {self.getModalidad()}")

# get y set

    def getmodalidad(self):
        return self._modalidad
    
    def getnum_empleado(self):
        return self._num_empleado
        
    
    def setmodalidad(self, modalidad):
        self._modalidad = modalidad

    def setnum_empleado(self, num_empleado):
        self.num_empleado = num_empleado