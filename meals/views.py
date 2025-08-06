from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_meals(request):
    return HttpResponse("Hello, meal!")