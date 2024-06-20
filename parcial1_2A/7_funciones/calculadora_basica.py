<<<<<<< HEAD
# print("..:::calculadora basica:::..")
# print("que operacion desear realizar:")
# print("1.- suma")
# print("2.- resta")
# print("3.- multiplicacion")
# print("4.- division")
# print("5.- salir")

# opcion = input("elije una opcion: ").upper()

# if opcion == "1" or opcion == "+" or opcion == "SUMA":

#  n1 = int(input("numero 1: "))
#  n2 = int(input("Numero 2: "))
#  suma = n1 + n2
#  print(f"{n1}+{n2}={suma}")

# elif opcion == "2" or opcion == "-" or opcion == "RESTA":

#  n1 = int(input("numero 1: "))
#  n2 = int(input("Numero 2: "))
#  suma = n1 - n2
#  print(f"{n1}-{n2}={suma}")

# elif opcion == "3" or opcion == "*" or opcion == "MULTIPLICACION":

#  n1 = int(input("numero 1: "))
#  n2 = int(input("Numero 2: "))
#  suma = n1 * n2
#  print(f"{n1}*{n2}={suma}")

# elif opcion == "4" or opcion == "/" or opcion == "DIVISION":

#  n1 = int(input("numero 1: "))
#  n2 = int(input("Numero 2: "))
#  suma = n1 / n2
#  print(f"{n1}/{n2}={suma}")

# else:
#     print("..::gracias por utilizar mi sistema::..")

import os 
    
def solicitarNumeros():
    global n1,n2
    n1=int(input("Numero # 1:"))
    n2=int(input("Numero # 2:"))

def calculadora(n1,n2,opcion):
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
        
        return f"{n1}+{n2}={n1+n2}"
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        
        return f"{n1}-{n2}={n1-n2}"
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
       
        return f"{n1}*{n2}={n1*n2}"
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        
        return f"{n1}/{n2}={n1/n2}"
    else:
        opcion=False
        return "Gracias por utilizar el sistema ..."
          
os.system("cls")

opcion=True
while opcion:

    os.system("cls")
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()
    if opcion != "5":
     solicitarNumeros()
     print(calculadora(n1,n2,opcion))
     def espereTecla() :
      espereTecla()
    else:
        opcion = False
=======
# print("..:::calculadora basica:::..")
# print("que operacion desear realizar:")
# print("1.- suma")
# print("2.- resta")
# print("3.- multiplicacion")
# print("4.- division")
# print("5.- salir")

# opcion = input("elije una opcion: ").upper()

# if opcion == "1" or opcion == "+" or opcion == "SUMA":

#  n1 = int(input("numero 1: "))
#  n2 = int(input("Numero 2: "))
#  suma = n1 + n2
#  print(f"{n1}+{n2}={suma}")

# elif opcion == "2" or opcion == "-" or opcion == "RESTA":

#  n1 = int(input("numero 1: "))
#  n2 = int(input("Numero 2: "))
#  suma = n1 - n2
#  print(f"{n1}-{n2}={suma}")

# elif opcion == "3" or opcion == "*" or opcion == "MULTIPLICACION":

#  n1 = int(input("numero 1: "))
#  n2 = int(input("Numero 2: "))
#  suma = n1 * n2
#  print(f"{n1}*{n2}={suma}")

# elif opcion == "4" or opcion == "/" or opcion == "DIVISION":

#  n1 = int(input("numero 1: "))
#  n2 = int(input("Numero 2: "))
#  suma = n1 / n2
#  print(f"{n1}/{n2}={suma}")

# else:
#     print("..::gracias por utilizar mi sistema::..")

import os 
    
def solicitarNumeros():
    global n1,n2
    n1=int(input("Numero # 1:"))
    n2=int(input("Numero # 2:"))

def calculadora(n1,n2,opcion):
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
        
        return f"{n1}+{n2}={n1+n2}"
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        
        return f"{n1}-{n2}={n1-n2}"
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
       
        return f"{n1}*{n2}={n1*n2}"
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        
        return f"{n1}/{n2}={n1/n2}"
    else:
        opcion=False
        return "Gracias por utilizar el sistema ..."
          
os.system("cls")

opcion=True
while opcion:

    os.system("cls")
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicacion \n 4.- División \n 5.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()
    if opcion != "5":
     solicitarNumeros()
     print(calculadora(n1,n2,opcion))
     def espereTecla() :
      espereTecla()
    else:
        opcion = False
>>>>>>> 25859170a0c301bb74334622a8104cfe9d1ef047
        print("gracias por utilizar el sistema")