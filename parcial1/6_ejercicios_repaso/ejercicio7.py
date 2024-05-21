# Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

# print(input("numero 1: "))
# print(input("numero 2: "))

# print("todos los numeros impares son:")
# for num_impar in range (1,20,2):

#     print(num_impar)

def numeros_impares(num1, num2):
    # Asegurarse de que num1 sea menor que num2
    if num1 > num2:
        num1, num2 = num2, num1
    
    print("Números impares entre", num1, "y", num2, "son:")
    for i in range(num1, num2 + 1):
        if i % 2 != 0:
            print(i)


# Solicitar al usuario los dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Llamar a la función para mostrar los números impares
numeros_impares(num1, num2)