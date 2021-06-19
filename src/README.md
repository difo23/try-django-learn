---
title: "Python Django Web Framework"
day: "1"
publishDate: "2021-06-18"
thumbnailImage: ""
shareText: " Description: Learn the Python Django framework with this free full course. Django is an extremely popular and fully featured server-side web framework, written in Python. Django allows you to quickly create web apps.  "
hashtags: ['learn', 'python', 'django']
draft: false


---

# Notes course Python Django Web Framework - freeCodeCamp.org 

| Source:      | https://youtu.be/F5mRW0jo-U4                                 |
| ------------ | ------------------------------------------------------------ |
| **Course:**  | Python Django Web Framework                                  |
| **Teacher:** | [ freeCodeCamp.org](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ) |



 ## 3- Setup your Virtual Environment for Django

### Create virtual env with python 3: 

``virtualenv -p python3 .``

### Activate virtual env:

``source bin/activate``

### Desactivate virtual env:

``deactivate``

### Install django:

``pip install django==2.0.7``

## 4- Create black django project:
```bash

  mkdir src
  cd src

```

```bash

../bin/django-admin startproject try_django_learn . 
python manage.py runserver

```

### See all packages install in the env:

``pip freeze``   

### Migrate 

Sep up all settings in the project.

```bash
 python manage.py migrate

```
### Create super user 

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


## 8 - Your First App Component

```bash 

python manage.py startapp products
#python manage.py startapp blog
#python manage.py startapp profiles
#python manage.py startapp cart

```

Thoses commands always came after create an apps in django:

``python manage.py makemigrations``   
``python manage.py migrate``

>> Note: The two commands use always that you change some model 

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

## 9- Create Product Objects in the python shell

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



## 11- New Models fields

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



## 12- Default Homepage to custom homepage:

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



## 13- URL Routing and requests

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

## 14- Django Templates

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



## 15- Django template engine basics

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

## 16- Include Template Tag include

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
    {% include 'navbar.html'}
    
    {% block content %}
    	replace me!
    {% endblock %}
    
</body>
</html>

```

Create `src/templates/navbar.html`



## 17- Rendering Context in a template

Add in ``src/pages/view.py`
```python
def home_view(request, *args, **kwargs):
  print(args, kwargs)
  print(request.user)
  my_context = {
      "my_text"     : "This is about us",
      "description" : "This is a description",
      "list_items"  : [1, 2, 3, 4]  
  }
  #return HttpResponse("<h1>Contact!</h2>")
  return render(
      request,
      "home.html", # Name template
      my_context
  )

```


Add to ``src/templates/home.html``
```html
{% extends 'base.html' %}

{% block content %}
<h1>
    Hello World from template
</h1>

<p>
    {{my_text}}, {{description}}
</p>
{% endblock %}
```

## 18- For Loop in a template

Add to ``src/templates/home.html`

```html
{% extends 'base.html' %}

{% block content %}
<h1>
    Hello World from template
</h1>

<p>
   {% for list_item in list_items %}
    <li> {{forloop.counter}}-{{ list_item}}</li>
   {% endfor %}
</p>
{% endblock %}
```

## 19 - Using Conditions in a Template

Add to ``src/templates/home.html`

```html
{% extends 'base.html' %}

{% block content %}
<h1>
    Hello World from template
</h1>

<p>
   {% for list_item in list_items %}
    {% if list_item == 23%}
		<p>Hola mundo!</p>
    {% endif %}
    <li> {{forloop.counter}}-{{ list_item}}</li>
   {% endfor %}
</p>
{% endblock %}
```

[More info...](https://docs.djangoproject.com/en/3.2/topics/templates/)

## 20  - Template Tags and Filters

Add to ``src/templates/home.html`

```html
{% extends 'base.html' %}

{% block content %}
<h1>
{{my_text | capfirst | upper }}
    Hello World from template
</h1>

<p>
   {% for list_item in list_items %}
    {% if list_item == 23%}
		<p>Hola mundo!</p>
    {% endif %}
    <li> {{forloop.counter}}-{{ list_item}}</li>
   {% endfor %}
</p>
{% endblock %}
```

[More info...](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#ref-templates-builtins-filters)

Note: The filter is very powerful 

##  21 - Render Data from the Database with a Mode

Use the shell

```bash
python manage.py shell
>>> from products.models import Product
>>> obj = Product.objects.get(id = 1)
>>> dir(obj)
```

Add in `src/products/views.py`

```python
# all defaults and old imports 
import .models import Product

def product_detail_view(request):
    obj = Product.objects.get(id = 1)
    context = {
        "title" : obj.title,
        "description" : obj.description
    }
    # Create in template/product/detail.html
    return render(
        request, 
        "product/detail.html", 
        context
    )


```

Add in `try_django_learn/urls.py`

```python
# all others imports
# import products views
form products.views import product_detail_view

urlpatterns = [
    # all paths
    path('product/', product_detail_view),
    # admin path
]
```

Create in `template/product/detail.html`

```html
{% extends 'base.html' %}

{% block content %}
<h1>
    Hello World from template
</h1>

<p>
  
    {% if description != None %}
		{{description}}
    {% endif %}
   <p>Hola mundo!</p>
  
</p>
{% endblock %}
```



## 22 - How Django Templates Load with Apps

 ([1:59:55](https://www.youtube.com/watch?v=F5mRW0jo-U4&t=7195s)) You need to see the tutorial in youtube

## 23 - Django Model Forms

Create a `try_django_learn/forms.py`

```python
from django import forms
from .models export Product

class ProductForm(forms.ModelForm):
    class Meta: 
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    

```

Add in `src/products/views.py`

```python
# all defaults and old imports 

import .forms import ProductForms 

def product_create_view(resquest):
    form = ProductForm(resquest.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)

    
#Old views
def product_detail_view(request):
  #all old code

```

Create ``template/products/product_create.html``

```html
{% extends 'base.html' %}

{% block content %}
<form method = 'POST'> {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value= "save"/> 
</form>
{% endblock %}
```

Add in `try_django_learn/urls.py`

```python
# all others imports
# import products views
form products.views import product_detail_view, product_create_view

urlpatterns = [
    # all paths
    path('create/', product_create_view),
    # admin path
]
```

## 24 - Raw HTML Form

