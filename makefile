.PHONY: up down migrate makemigrations restart logs

up:
	docker compose up -d
	docker compose exec web python manage.py migrate

down:
	docker compose down

migrate:
	docker compose exec web python manage.py migrate

makemigrations:
	docker compose exec web python manage.py makemigrations

restart:
	docker compose down
	docker compose up -d

logs:
	docker compose logs -f
