# Usa una imagen de Python 3.8
FROM python:3.8

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que la aplicación está ejecutando
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["python", "app.py"]

