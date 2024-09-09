pip install django==4.2
python -m django --version


## Create Project
django-admin startproject movieapi

python manage.py runserver
python manage.py runserver 8080
python manage.py runserver 0.0.0.0:8080

python manage.py startapp movies

## Migrations
python manage.py showmigrations
python manage.py makemigrations
python manage.py migrate

python manage.py showmigrations movies
python manage.py makemigrations movies
python manage.py migrate movies