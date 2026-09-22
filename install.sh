#!/usr/bin/env bash

set -e

echo "Building Docker containers..."
docker compose build

echo "Starting PostgreSQL and Django..."
docker compose up -d

echo "Waiting for PostgreSQL..."
until docker compose exec -T postgres pg_isready \
    -U "${DB_USER}" \
    -d "${DB_NAME}" > /dev/null 2>&1
do
    sleep 1
done

echo "PostgreSQL is ready."

echo "Creating migrations..."
docker compose exec web python manage.py makemigrations

echo "Applying migrations..."
docker compose exec web python manage.py migrate

echo "Collecting static files..."
docker compose exec web python manage.py collectstatic --noinput

echo "Installation complete."
echo "Open http://localhost"
