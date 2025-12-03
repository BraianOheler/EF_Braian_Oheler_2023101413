import pymysql

def get_db_connection():
    return pymysql.connect(
        host='localhost',       # Cambia por tu host si es necesario
        user='root',            # Usuario MySQL
        password='root',        # Contraseña MySQL
        database='ganaderia',   # Nombre de tu base de datos
        port=3307,              # Puerto de MySQL Express
        cursorclass=pymysql.cursors.DictCursor  # Para recibir diccionarios (opcional pero útil)
    )
