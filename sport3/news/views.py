from django.shortcuts import render
from .models import MyNewsFb
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('this is home')
