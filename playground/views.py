from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# takes request -> returns response
# in other frameworks, a view is called a request handler or action

def say_hello(request):
  return HttpResponse('Hello world!')

def send_html(request):
  return render(request, 'hello.html', {'name': 'Blake'})