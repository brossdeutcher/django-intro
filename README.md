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

## commands
``` django-admin ``` performs admin commands before project initiated

``` python manage.py ``` performs admin functions after project initiated