import mysql.connector

#Conexion con la BD de MySQL
try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_python'
    )
except Exception as e:
    print(f"Ocurrio un error por favor vuelva a verificar...mas tarde...")
