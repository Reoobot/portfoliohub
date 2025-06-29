FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    default-mysql-client \
    gcc \
    netcat-traditional \
    && pip install --no-cache-dir -r requirements.txt



COPY . .

# Copiar el script de entrada
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Usar el script como punto de entrada
ENTRYPOINT ["/app/entrypoint.sh"]
