import os
import re
from database import get_connection, init_db

def validate_email(email):
    """
    Validación estricta de entrada (Input Validation).
    Utiliza una expresión regular para asegurar que el formato sea un correo real
    antes de interactuar con cualquier base de datos o sistema.
    """
    # Patrón estándar para correos electrónicos básicos
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not email or not isinstance(email, str):
        return False
    return re.match(pattern, email) is not None

def insert_record(name, email, data_payload):
    """
    Inserta un nuevo registro en la base de datos de manera segura.
    Garantiza inmunidad contra Inyección SQL mediante consultas parametrizadas.
    """
    # 1. Aplicar la validación antes de procesar el registro
    if not validate_email(email):
        raise ValueError(f"Falla de Seguridad: Formato de email inválido ('{email}').")
    
    # 2. Consulta parametrizada (Los datos nunca se concatenan directamente en el string)
    query = """
        INSERT INTO records (name, email, data_payload) 
        VALUES (%s, %s, %s);
    """
    
    # 3. Ejecución segura dentro del contexto de conexión
    with get_connection() as conn:
        with conn.cursor() as cur:
            # Los parámetros se envían por separado a la base de datos
            cur.execute(query, (name, email, data_payload))
            conn.commit()

if __name__ == "__main__":
    print("[LOG] Inicializando componentes de seguridad...")
    try:
        # Intentará inicializar la base de datos (requiere variables de entorno configuradas)
        init_db()
        print("[LOG] Base de datos inicializada correctamente.")
    except Exception as e:
        print(f"[ALERTA] No se pudo conectar a la base de datos: {e}")
        print("[INFO] Esto es normal si aún no hemos levantado el contenedor de PostgreSQL.")
