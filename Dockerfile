# Usar una imagen Alpine ultra-segura y limpia
FROM python:3.10-alpine

# Instalar dependencias del sistema necesarias para crear usuarios en Alpine
RUN apk add --no-cache shadow

# Crear un usuario del sistema sin privilegios
RUN useradd -m appuser
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

USER appuser

CMD ["python", "src/app.py"]
