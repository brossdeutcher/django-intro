# Intro to Django

From following this
[YouTube video](https://www.youtube.com/watch?v=rHux0gMZ3Eg&list=WL&index=41&t=627s)

## set-up
1. install pipenv to create a virtual environment
```
pip3 install pipenv
```
2. install Django in pipenv virtual environment
```
pipenv install django
```
3. activate virtual environment (zsh changes to python3)
```
pipenv shell
```
4. start the Django project (. at the end avoids creating a redundant folder)
```
django-admin startproject projectname .
```
5. run the server (optional: server number after runserver if want to specify port)
```
python manage.py runserver
```

## useful commands
``` django-admin ``` performs admin commands before project initiated

``` python manage.py ``` performs admin functions after project initiated

``` pipenv --venv ``` prints file path to virtual environment when used in virtual environment

## apps from INSTALLED_APPS in settings.py

django.contrib.admin - gives admin interface for managing data

django.contrib.auth - used for authenticating users

django.contrib.contenttypes - 

django.contrib.sessions - legacy app that can be deleted

django.contrib.messages - used for one-time notifications to end user

django.contrib.staticfiles - used for serving static files

- create a new app
```
python manage.py startapp appname
```
- register app ~ add the appname to INSTALLED_APPS in settings.py

## views from views.py in an app (similar to a request/response handler)

often called request handler or action in other frameworks, views in Django handle http requests and responses

views.py | basic view function to handle the request and response
```
from django.http import HttpResponse

def function_name(request):
  return HttpResponse('response')
```

urls.py | urlpatterns is a list Django looks for that contains url path functions with the endpoint & view function
```
from django.urls import path
from . import views

urlpatterns = [
  path('hello/', views.say_hello)
]
```