from django.shortcuts import render
from django.http import HttpResponse   #imported http module
# Create your views here.

def index(request):  #this is a function based view processing request
    return HttpResponse("This is working!!")   #returning with a response