#!/bin/bash

# Преобразуем концы строк в Unix-формат
sed -i 's/\r$//' /entrypoint.sh

# Ожидаем запуска базы данных
echo "Waiting for PostgreSQL to be ready..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 1
done

# Применяем миграции
python manage.py makemigrations shop
python manage.py migrate

# Собираем статические файлы
python manage.py collectstatic --noinput

# Запускаем Gunicorn
exec gunicorn --bind 0.0.0.0:8000 shopProject.wsgi:application