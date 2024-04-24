from django.urls import path
from . import views

# URLConf module | django looks for this name, so spell it right
urlpatterns = [
  path('hello/', views.say_hello), # path() takes two parameters: the endpoint & the view function (without parentheses)
  path('html/', views.send_html)
]