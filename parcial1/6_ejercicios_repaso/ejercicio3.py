# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for

# for

print("los cuadrados de los 60 primeros numeros naturales son: ")
for num_naturales in range (1,61):
    cuadrados = num_naturales ** 2
    print(num_naturales,"² = ",cuadrados)


# while

cont = 0
suma = 0

while cont <= 59 :
 
 suma += cont
 cont += 1

 cuadradoss = cont ** 2
 print(cont,"² = ",cuadradoss) 
 
