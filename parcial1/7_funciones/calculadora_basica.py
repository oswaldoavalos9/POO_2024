print("..:::calculadora basica:::..")
print("que operacion desear realizar:")
print("1.- suma")
print("2.- resta")
print("3.- multiplicacion")
print("4.- division")
print("5.- salir")

opcion = input("elije una opcion: ").upper()

if opcion == "1" or opcion == "+" or opcion == "SUMA":

 n1 = int(input("numero 1: "))
 n2 = int(input("Numero 2: "))
 suma = n1 + n2
 print(f"{n1}+{n2}={suma}")

elif opcion == "2" or opcion == "-" or opcion == "RESTA":

 n1 = int(input("numero 1: "))
 n2 = int(input("Numero 2: "))
 suma = n1 - n2
 print(f"{n1}-{n2}={suma}")

elif opcion == "3" or opcion == "*" or opcion == "MULTIPLICACION":

 n1 = int(input("numero 1: "))
 n2 = int(input("Numero 2: "))
 suma = n1 * n2
 print(f"{n1}*{n2}={suma}")

elif opcion == "4" or opcion == "/" or opcion == "DIVISION":

 n1 = int(input("numero 1: "))
 n2 = int(input("Numero 2: "))
 suma = n1 / n2
 print(f"{n1}/{n2}={suma}")

else:
 print("..::gracias por utilizar mi sistema::..")