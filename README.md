# Pipeline Automatizado para Procesamiento Seguro de Datos (DevSecOps)

## Descripción del Proyecto
Este proyecto implementa un flujo automatizado (Pipeline) diseñado para la recepción, validación y almacenamiento seguro de registros de información. Aplica metodologías **DevSecOps** bajo el concepto de *Shift Left Security* (Seguridad desde el inicio), automatizando el escaneo de vulnerabilidades y previniendo la inyección de datos maliciosos.

## Mecanismos de Ciberseguridad Implementados
*   **Validación Estricta de Entradas:** Expresiones regulares en el código para filtrar y rechazar correos corruptos antes de procesarlos.
*   **Mitigación de Inyección SQL (SQLi):** Uso obligatorio de consultas parametrizadas a través del conector nativo de la base de datos.
*   **Principio de Mínimos Privilegios (Dockerfile Hardening):** Ejecución del contenedor bajo un usuario del sistema sin privilegios (`appuser`), evitando el uso de `root`.
*   **Auditoría de Código (SAST):** Análisis estático automatizado con `Bandit` integrado en el ciclo de integración continua.
*   **Escaneo de Contenedores (SCA):** Análisis profundo de dependencias y vulnerabilidades en la imagen Docker utilizando `Trivy`.

## Tecnologías Utilizadas
*   **Lenguaje:** Python 3.10+
*   **Orquestación y CI/CD:** GitHub Actions
*   **Contenedores:** Docker (PostgreSQL 15 Alpine)
*   **Seguridad / SAST:** Bandit & Trivy

## Ejecución de Pruebas Unitarias
Para validar localmente la suite de pruebas anti-inyección, ejecuta dentro de tu entorno virtual:
```bash
python -m unittest discover -s tests
```
