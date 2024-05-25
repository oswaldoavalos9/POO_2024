# crear un programa que permita imprimir el precio a pagar por un artuculo.
# en el precio a pagar se incluye el IVA. el programa debera de funcionar n veces como el usuario decee



while True:
    try:
        precio_sin_iva = float(input("Ingrese el precio del artículo sin IVA: ")) 
        
        precio_con_iva = precio_sin_iva * 1.16
            
        print(f"El precio a pagar por el artículo con IVA incluido es: {precio_con_iva:.2f}")
    except ValueError:
            print("Por favor, ingrese un número válido.")
        
    continuar = input("¿Desea calcular el precio de otro artículo? (si/no): ")
    if continuar.lower() != 'si':
            break
