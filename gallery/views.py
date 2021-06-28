from django.shortcuts import render,redirect
from .models import Gallery
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.models import User
# Create your views here.
def homepage(request):
  return render(request,'gallery/index.html')
  
