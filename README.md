# Django Docker App

A basic Django web app with PostgreSQL, Gunicorn, and Docker.

## Project Structure

```
django-docker-app/
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env.example
├── manage.py
├── requirements.txt
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
└── templates/
    └── core/
        └── home.html
```

## Quick Start

```bash
# 1. Start all services
docker-compose up --build

# 2. Create a superuser (in a new terminal)
docker-compose exec web python manage.py createsuperuser

# 3. Visit the app
open http://localhost:8000

# 4. Visit the admin
open http://localhost:8000/admin
```

## Common Commands

```bash
# Run migrations
docker-compose exec web python manage.py migrate

# Make new migrations
docker-compose exec web python manage.py makemigrations

# Django shell
docker-compose exec web python manage.py shell

# Stop services
docker-compose down

# Stop and remove volumes (wipes database)
docker-compose down -v
```
