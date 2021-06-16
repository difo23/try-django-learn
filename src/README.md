
# Notes course Python Django Web Framework - freeCodeCamp.org 

## Create virtual env with python 3: 

``virtualenv -p python3 .``

## Activate virtual env:
  
``source bin/activate``

## Desactivate virtual env:

``deactivate``

## Install django:

``pip install django==2.0.7``

## Create black django project:
```bash

  mkdir src
  cd src

```

```bash

../bin/django-admin startproject try_django_learn . 
python manage.py runserver

```

## See all packages install in the env:

``pip freeze``   

## Migrate 

Sep up all settings in the project.

```bash
 python manage.py migrate

```
## Create super user 

```bash

python manage.py createsuperuser

```
```
  pass: rast*****
  email: diffozanzan@gmail.com
  user: difo23
```

I can to use ``http://localhost:8000/admin/``


Note: the ``manage.py`` is a very important file. You need to use this in all manager commands. 


## Create apps

```bash 

python manage.py startapp products
python manage.py startapp blog
python manage.py startapp profiles
python manage.py startapp cart

```

This commands always came after create an apps in django:

``python manage.py makemigrations``   
``python manage.py migrate``

>> Note: The two commands use always that you change some model o other things

1. Add in ``products/models``    
   
   ```py
        from django.db import models


        class Product(models.Model):
            title       = models.TextField()
            description = models.TextField()
            price       = models.TextField()

   ```

2. Add in ``products/admin.py``    
   
   ```py

      from django.apps import AppConfig

      class ProductsConfig(AppConfig):
          name = 'products'

   ```
3.  Add in  ``src/try_django_learn/settings``        
    ```py
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',

            #third party 

            #my owns apps
            'products',
          ]

    ```

