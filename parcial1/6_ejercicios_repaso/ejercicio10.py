# crear un programa que solicite la calificacion de 15 alumnos
# e imprima en pantalla cuantos aprobaron y cuantos no aprovaron


calificaciones = []
aprobados = 0
reprobados = 0

for i in range(15):
    calificacion = float(input(f"Ingrese la calificación del alumno  {i+1}: " ))
    calificaciones.append(calificacion)

for calificacion in calificaciones:
    if calificacion >= 8:
        aprobados += 1
    else:
        reprobados += 1
print("")
print(f"Alumnos que aprobaron: {aprobados}")
print(f"Alumnos que no aprobaron: {reprobados}")