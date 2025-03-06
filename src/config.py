import psycopg2

def get_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="CULTIVARED",
            user="admin",
            password="1234"
        )
        connection.autocommit = True  # Habilitar autocommit
        return connection
    except Exception as ex:
        print("Error de conexión:", ex)
        return None

