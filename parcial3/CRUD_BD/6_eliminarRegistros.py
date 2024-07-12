from conexionBD import *


try:
    micursor=conexion.cursor()
    sql="DELETE FROM clientes where id=1"


    micursor.execute(sql)
    #Es necesario ejecutar el *commit* para que finalice el SQL con exito
    #INSERT, UPDATE & DELETE
    conexion.commit()
except:
    print(f"Ocurrio un error por favor vuelva a intentar...mas tarde...")
else:
    print("Registro eliminado con exito")