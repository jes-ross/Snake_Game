''' 
Jesus Rosales Santana
12-02-2023
Conexión a base de datos
'''

import psycopg2 #Con esta libreria nos podremos conectar a postgres

try:
    conection = psycopg2.connect(database= "BaseDatos_Prueba", user= "postgres", password= "Contraseña_Prueba")#Con esta linea de comandos nos conectamos a la base
    cursor = conection.cursor()
    cursor.execute("select version()")
    version = cursor.fetchone()
except Exception as err:
    print("Error al conectar la base", err)

else:
    print(version)

def insert_valores():
    cursor = conection.cursor()
    query = f"""INSERT INTO informacion(id, nombre, edad, colegio) values(1, 'luis', 12, 'almeria')"""
    cursor.execute(query)
    cursor.close()


insert_valores()
conection.close()
