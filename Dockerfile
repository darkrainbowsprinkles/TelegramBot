# Usar una imagen base de Python
FROM python:3.12-slim

# Crear carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Instalar dependencias si hubiera (requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt || echo "No requirements"

# Comando por defecto: ejecutar el script
CMD ["python", "mi-bot.py"]
