# crear un programa que permita imprimir el precio a pagar por un artuculo.
# en el precio a pagar se incluye el IVA. el programa debera de funcionar n veces como el usuario decee



while True:
    precio_s_IVA = int(input("¿cual es el precio del articulo? "))

    precio_c_IVA = (precio_s_IVA * 0.16) + precio_s_IVA
    print("el precio de tu producto con iva es: ",precio_c_IVA)

    continuar = input("¿Desea calcular el precio de otro artículo? (si/no): ")
    

    if continuar == ("no"):
        print("Saliendo del programa...")
        break
