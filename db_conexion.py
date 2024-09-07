#Conexion a base de datos

import psycopg2

#Importar modulos para usar llaves seguras
from dotenv import load_dotenv
import os

load_dotenv()

#Establecer parametro de conexion

dbname= os.getenv('DBNAME')
user=os.getenv('USER')
password=os.getenv('PASSWORD')
host=os.getenv('HOST') #Si fuera remoto la direccion ip de postgres
port=os.getenv('PORT')

#conectar base de datos

try:
    conn = psycopg2.connect(dbname=dbname, user=user,password=password,host=host,port=port)
    print('Conexion de base de datos exitoso')
    #Crear el cursos
    cur=conn.cursor()
    #Consulta la base de datos

 # Crear la tabla
    cur.execute('CREATE TABLE productos ( \
    id SERIAL PRIMARY KEY, \
    nombre VARCHAR(100) NOT NULL, \
    precio NUMERIC(10,2) \
    );')
    
    conn.commit()  # Confirmar los cambios
    print("Tabla 'productos' creada exitosamente.")

# Cerrar el cursor y la conexión
    cur.close()

except psycopg2.Error as error:
    print('Error al establecer la conexion: ', error)

finally:
    #Cerrar la conexion
    if conn is not None:
        conn.close()
        print('Conexion cerrada')



