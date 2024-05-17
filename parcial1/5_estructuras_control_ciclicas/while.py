contador = 1
while contador <= 5:
    print("@")
    contador += 1



contador = 1
suma = 0

while contador <= 5 :
    print(contador)
    suma += contador
    contador += 1

print("la suma es: ",suma)

tabla=int(input("ingrea un numero para calcular su tabla de multiplicar: "))
i = 1
multi = 0 
while i <= 10:
    multi = i * tabla
     
    print(tabla, "x", i, "=", multi)
    i += 1