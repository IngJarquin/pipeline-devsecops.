import os
import psycopg2
from psycopg2 import sql

def get_connection():
    """
    Establece la conexión a PostgreSQL de forma segura.
    Los secretos nunca se guardan en el código; se extraen del entorno.
    """
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "secure_db"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT", "5432")
    )

def init_db():
    """
    Inicializa la estructura de la tabla si no existe en la base de datos.
    """
    query = """
    CREATE TABLE IF NOT EXISTS records (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100) UNIQUE,
        data_payload TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
