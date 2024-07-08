from coches import *

print("Objeto 1")
coche1=Coches(f"Blanco","VW","2022",220,150,5)

coche1.getInfo()


print("Objeto 2")
coche2=Coches(f"Azul","Nissan","2020",180,150,6)
coche2.getInfo()



#implementar el encapsulamiento o visibilidad

print(coche1.atributo_publico)
# print(coche1.__atributo_privado) #No es posible
print(coche1.MetodoPublico())


# coche1.__MetodoPrivado() #No es posible
coche1.getMetodoPublico()