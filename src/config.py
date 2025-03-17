import psycopg2

# Configuración de conexión a la base de datos
DB_CONFIG = {
    "dbname": "cultivared",
    "user": "postgres",
    "password": "12345",
    "host": "34.172.195.227",
    "port": "5432"
}

# Función para obtener conexión
def get_connection():
    try:
        return psycopg2.connect(**DB_CONFIG)
    except Exception as e:
        print("Error de conexión:", e)
        return None

# Probar conexión
conn = get_connection()
if conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("Conectado a:", db_version)
    conn.close()


