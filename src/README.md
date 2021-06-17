

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
  email: dif*******@gmail.com
  user: difo23
```

I can to use ``http://localhost:8000/admin/``


Note: the ``manage.py`` is a very important file. You need to use this in all manager commands. 


## Create apps

```bash 

python manage.py startapp products
#python manage.py startapp blog
#python manage.py startapp profiles
#python manage.py startapp cart

```

Thoses commands always came after create an apps in django:

``python manage.py makemigrations``   
``python manage.py migrate``

>> Note: The two commands use always that you change some model o other things

1. Add in ``products/models``    


```python
    from django.db import models
    
    class Product(models.Model):
        title       = models.TextField()
        description = models.TextField()
        price       = models.TextField()
       
```

2. Add in ``products/admin.py``

```python
from django.apps import AppConfig

class ProductsConfig(AppConfig):
     name = 'products'

```
3.  Add in  ``src/try_django_learn/settings``        
```python
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

## Create Product Objects in the python shelL

```bash
  python manage.py shell
```
```py
>>> from products.models import Product
>>> Product.objects.all()
>>> Product.objects.create(
...   title='New product-Shell', 
...   description = 'Another object test',
...   price = '1902',
... )
```



## New Models fields

Origin

```python
class Product(models.Model):
        title       = models.TextField()
        description = models.TextField()
        price       = models.TextField()
```

Add different types of fields

```python
class Product(models.Model):
    title  		= models.CharField( max_length = 120 ) # max_length is required
    desciption 	= models.TextField( blank = True, null = True ) #Blank is for empty or not empty 
    summary		= models.TextField( defalult = 'this is cool!' )
    price = models.DecimalField( decimal_places = 2, max_digits = 10000 )
    
    
```

[More about models-fields](https://docs.djangoproject.com/en/3.2/ref/models/fields/#model-field-types)

Validate changes with

``python manage.py makemigrations``   
``python manage.py migrate``



## Default Homepage to custom homepage:

```
python manage.py startapp pages

```

Add in  ``src/try_django_learn/settings.py``

```
#my owns apps
'products',
'pages',
```

Add in ``src/pages/view.py``

```python
from django.http import HttpResponse
from django.shortcuts import render

def home_view(*args, **kwargs):
  return HttpResponse("<h1>Hello wold!</h2>")
```

Add urls in ``src/try_django_learn/urls.py ``

```python
from django.contrib import admin
from django.urls import path

from pages.views import home_view

urlpatterns = {
    path('', home_view, name = 'home'),
    path('admin/', admin.site.urls),
    
}
```



## URL Routing and requests

Add in ``src/pages/view.py``

```python
def contact_view(request, *args, **kwargs):
  print(args. kwargs)
  print(resquest.user)
  return HttpResponse("<h1>Contact!</h2>")
```

Add urls in ``src/try_django_learn/urls.py ``

```python
from django.contrib import admin
from django.urls import path

from pages.views import home_view, contact_view

urlpatterns = {
    path('', home_view, name = 'home'),
    path('contact/', contact_view, name = 'contact'),
    path('admin/', admin.site.urls),
    
}
```

## Django Templates

Add in ``src/pages/view.py``

```python
def home_view(request, *args, **kwargs):
  print(args. kwargs)
  print(resquest.user)
  #return HttpResponse("<h1>Contact!</h2>")
  return render(
      request,
      "home.html", # Name template
      {}
  )
```

Add in ``src/template/home.html``

```html
<h1>
     Hello World from template
</h1>

<p>
    {{request.user}}
</p>
```

Add in ``src/try_django_learn/settings.py``

```python

#TEMPLATES_PATH = f"{BASE_DIR}/templates"
TEMPLATES_PATH = os.path.join(BASE_DIR, "templates")
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_PATH],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


```



## Django template engine basics

Use  default structure in django ``base.html`` base is a convention

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> Django template structure </title>
</head>
<body>
    
    
    {% block content %}
    	replace me!
    {% endblock %}
    
</body>
</html>

```

Add chunk to ``src/templates/home.html``

```html
{% extends 'base.html' %}

{% block content %}
<h1>
    Hello World from template
</h1>

<p>
    {{request.user}}
</p>
{% endblock %}
```

