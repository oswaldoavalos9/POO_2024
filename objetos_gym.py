from personas import *

# personal_limpieza

personal_limpieza1 = PersonalLimpieza("Pedro", "Picapiedra", 21, 1, "mañana", 900)

personal_limpieza2 = PersonalLimpieza("Cristian", "Rocha", 19, 2, "tarde", 850)

#  Cliente

cliente1 = Cliente("Oswaldo", "Avalos", 18, 1, 81, 1.82)

cliente2 = Cliente("Jonathan", "Tinoco", 19, 2, 78, 1.70)

# istructor

instructor1 = Instructor("Lincon", "Luna", 23, 1, "tarde", 1500)

instructor2 = Instructor("Teodoro", "Robles", 25, 2, "noche", 1800)


print("Información del Personal de Limpieza:")
print(f"Personal de Limpieza 1: {personal_limpieza1.nombre} {personal_limpieza1.apellido}, Edad: {personal_limpieza1.edad}, Horario: {personal_limpieza1.horario}, Sueldo: {personal_limpieza1.sueldo}")
print(f"Personal de Limpieza 2: {personal_limpieza2.nombre} {personal_limpieza2.apellido}, Edad: {personal_limpieza2.edad}, Horario: {personal_limpieza2.horario}, Sueldo: {personal_limpieza2.sueldo}")

print("\nInformación de los Clientes:")
print(f"Cliente 1: {cliente1.nombre} {cliente1.apellido}, Edad: {cliente1.edad}, Peso: {cliente1.peso}, Estatura: {cliente1.estatura}")
print(f"Cliente 2: {cliente2.nombre} {cliente2.apellido}, Edad: {cliente2.edad}, Peso: {cliente2.peso}, Estatura: {cliente2.estatura}")

print("\nInformación de los Instructores:")
print(f"Instructor 1: {instructor1.nombre} {instructor1.apellido}, Edad: {instructor1.edad}, Horario: {instructor1.horario}, Sueldo: {instructor1.sueldo}")
print(f"Instructor 2: {instructor2.nombre} {instructor2.apellido}, Edad: {instructor2.edad}, Horario: {instructor2.horario}, Sueldo: {instructor2.sueldo}")