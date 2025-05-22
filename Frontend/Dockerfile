# Dockerfile-frontend

#Image base
FROM python:3.9

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos de dependencias e instalar
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

CMD [ "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0" ]