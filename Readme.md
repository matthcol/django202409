pip install django==4.2
python -m django --version
pip install psycopg2
pip install django-extensions
pip install ipython
pip install jupyter jupyterlab notebook
pip install djangorestframework markdown django-filter

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

python manage.py migrate movies 0001
python manage.py migrate movies 0002
python manage.py migrate movies 0001
python manage.py migrate movies zero

python manage.py sqlmigrate movies 0001 (=> stdout)
python manage.py sqlmigrate movies 0001 > sql\001-movie-ddl.sql

python manage.py squashmigrations movies 0001 0004

## Python shell with Django ORM
python .\manage.py shell
python .\manage.py shell -i ipython

```
from movies.models import Movie
movies = Movie.objects.all()
m=movies 
m.title
m.year
```

## Python Shell plus (extensions)
### with UI ipython (or python)
python .\manage.py shell_plus (import auto)

```
movies = Movie.objects.all()
```


### with GUI lab or notebook
python .\manage.py shell_plus --lab
python .\manage.py shell_plus --notebook

NB: set environment variable DJANGO_ALLOW_ASYNC_UNSAFE

#### Command Dos
```
set DJANGO_ALLOW_ASYNC_UNSAFE=True
```

#### Powershell
```
${env:DJANGO_ALLOW_ASYNC_UNSAFE}="True"
```

#### Bash
```
export DJANGO_ALLOW_ASYNC_UNSAFE=True
```



## Docker
In directory docker\dbmoviempty

docker compose up -d