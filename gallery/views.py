from django.shortcuts import render,redirect
from .models import Gallery
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.models import User
# Create your views here.
def homepage(request):
  return render(request,'gallery/index.html')
  
@login_required(login_url='accounts:login')
def newsfeed(request):
  gallery=Gallery.objects.all().order_by('date')
  return render(request,'gallery/new.html',{'gallery':gallery})
  
def sharedetails(request,slug):
  gallery=Gallery.objects.get(slug=slug)
  return render (request,'gallery/gallerydetails.html',{'gallery':gallery})
@login_required(login_url='accounts:login') 
def createshare(request):
  if request.method=="POST":
    form=forms.CreateShare(request.POST,request.FILES)
    if form.is_valid():
      instance=form.save(commit=False)
      instance.author=request.user
      instance.save()
      return redirect('gallery:newsfeed')
    else:
      return redirect('gallery:create')
    
  
  else:
    form=forms.CreateShare()
  return render(request,'gallery/gallerycreate.html',{'form':form})
