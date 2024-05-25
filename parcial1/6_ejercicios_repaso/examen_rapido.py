#SIS - 100/120 normal, DIA - 60/80 normal

clientes = 0

print(".:bienvenido:.")

while True:
     
     clientes = clientes + 1

     input("nombre del pasiente: ")
     input("tipo de sangre: ")
     
     print("medicion SIStonica: ")
     sis1 = int(input("1er medicion: "))
     sis2 = int(input("2do medicion: "))
     sis3 = int(input("3er medicion: "))

     por_sis = (sis1 + sis2 + sis3) / 3
     print(por_sis)

     print("medicion DIAstonica: ")
     dia1 = int(input("1er medicion: "))
     dia2 = int(input("2do medicion: "))
     dia3 = int(input("3er medicion: "))

     por_dia = (dia1 + dia2 + dia3) / 3

     print("porcentajes: ")
     print(por_sis)
     print(por_dia)


     if por_sis <= 120 and por_dia <= 80 :
         
         print("estas sano")
     
     

     respuesta = input("¿deseas otra captura?(SI/NO) ")

     if respuesta == ("no"):
        print("Saliendo del programa...")
        break
     
print("clientes apendidos: ", clientes)
