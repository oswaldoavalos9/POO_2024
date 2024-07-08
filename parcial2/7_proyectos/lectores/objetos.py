from clases import *

print("estudiante 1")
estudiante1 = estudiantes("Ana Torez Guzman", "col. centro 1500 ote", "6181234567","MECA", "2325678")


print("docente 1")
docente1 = docentes("Daniel Fuentes Loera", "Fracc. D. Arriata 1400 nte", "6183335678", "TI", "123")

estudiante1.reservar()
docente1.reservar()