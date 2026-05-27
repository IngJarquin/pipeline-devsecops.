# 1. Usar una imagen base ligera y oficial para reducir la superficie de ataque
FROM python:3.10-slim

# 2. Crear un usuario del sistema sin privilegios para mitigar exploits de escalada de poder
RUN useradd -m appuser

# 3. Establecer el directorio de trabajo seguro
WORKDIR /app

# 4. Copiar e instalar dependencias antes del código (aprovecha la caché de Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el código fuente asegurando que pertenezca al usuario sin privilegios
COPY src/ ./src/

# 6. Cambiar el contexto de ejecución al usuario seguro
USER appuser

# 7. Comando por defecto para arrancar la aplicación de forma segura
CMD ["python", "src/app.py"]
