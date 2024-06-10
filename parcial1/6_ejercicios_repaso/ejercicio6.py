<<<<<<< HEAD
# Mostrar todas las tablas del 1 al 10.
# Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10


for num_tabla in range (1,11):
    print("tabla de multiplicar del: ",num_tabla)
    for contador in range (0,10):
         contador += 1
         resultado = contador * num_tabla
=======
# Mostrar todas las tablas del 1 al 10.
# Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10


for num_tabla in range (1,11):
    print("tabla de multiplicar del: ",num_tabla)
    for contador in range (0,10):
         contador += 1
         resultado = contador * num_tabla
>>>>>>> ddb1045bbb29ea5fca236c962e8dd2c8efc2216f
         print(num_tabla, "X ", contador , " = ",resultado)