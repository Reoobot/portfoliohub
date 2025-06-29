FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    default-mysql-client \
    gcc \
    && pip install --no-cache-dir -r requirements.txt



COPY . .

CMD ["gunicorn", "portfoliohub.wsgi:application", "--bind", "0.0.0.0:8000"]
