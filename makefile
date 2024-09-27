up:
	docker-compose up -d

build:
	docker-compose build

down:
	docker-compose down

down-v:
	docker-compose down -v

migrate:
	docker-compose rum --rm web python manage.py migrate

makemigrations:
	docker-compose rum --rm web python manage.py makemigrations

createsuperuser:
	docker-compose rum --rm web python manage.py createsuperuser
