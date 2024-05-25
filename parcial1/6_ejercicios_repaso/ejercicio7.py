# Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

# print(input("numero 1: "))
# print(input("numero 2: "))

# print("todos los numeros impares son:")
# for num_impar in range (1,20,2):

#     print(num_impar)

num1 = int(input("num1: "))
num2 = int(input("num2: "))


if num1 > num2:
        num1, num2 = num2, num1
    
print("Números impares entre", num1, "y", num2, "son:")
for i in range(num1, num2 + 1):
        if i % 2 != 0:
            print(i)
