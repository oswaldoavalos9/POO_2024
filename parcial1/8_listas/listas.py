"""

list (Array)
son coleciones o conjuntos de datos/valores bajo
un mismo nombre, para acceder a los valores se
hacevcon un indice numerico

nota: sus valores si son modificables

la lista es una coleccion ordenada y modificable. permite miembros duplicados


"""

# ejemplo 1 crear una lista con valores numericos enteros e imprimir la lista

numeros = [23, 34]
print(numeros)

# recorrer la lista con for

for i in numeros:
    print(i)

# recorrer la lista con while
i = 0
while i < len (numeros):
    print(numeros [i])
    i +=1

# crear una lista de palabras posteriormente ingresar una palabra
# para buscar la coincidencia en la lista e indicar si aparece la palabra y en que
# posicion caso contrario indicar una vez si no lo encontro

palabra = ["hola", "2024", "10.23", "True"]

palabra_buscar = input("ingresa la palabra buscar: ")
for palabra_buscar in palabra:
    