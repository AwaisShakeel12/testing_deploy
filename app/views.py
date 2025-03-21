from django.shortcuts import render

# Create your views here.
from .models import *

def home(request):
    cars = Cars.objects.all()
    
    
    
    return render(request, 'home.html', {'cars':cars})