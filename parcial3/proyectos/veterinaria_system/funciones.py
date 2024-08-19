import msvcrt
import os
import platform

def esperarTecla():
    print("")
    print("Presione cualquier tecla para continuar...")
    msvcrt.getch()

def limpiarPantalla():
    
    if platform.system() == "Windows": 
        os.system("cls") 
    else:
        os.system("clear")
    
    