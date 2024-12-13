FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    postgresql-client \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/staticfiles /app/media

ENV POSTGRES_HOST=db
ENV POSTGRES_PORT=5432
ENV POSTGRES_DB=medusashop_db
ENV POSTGRES_USER=medusashop_user
ENV POSTGRES_PASSWORD=medusashop_pass

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

RUN chmod -R 755 /app
RUN chown -R 1000:1000 /app
RUN chown -R 1000:1000 /app/staticfiles
RUN chown -R 1000:1000 /app/media

ENTRYPOINT ["/entrypoint.sh"]