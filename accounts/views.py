from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.hashers import make_password


# Create your views here.
def signup(request):
  if request.method == "POST":
    username=request.POST["username"]
    password=request.POST["pwd1"]
    password2=request.POST["pwd2"]
    

    user = User.objects.filter(username=username)

    if user.exists():
      messages.error(request, "User Already Exists with the same username ")
      return redirect('accounts:signup')

    elif password != password2:
      messages.error(request, "passwords must be the same ")
      return redirect('accounts:signup')

    elif username in User.objects.all():
      messages.error(request, "User Already Exists with the same username ")
      return redirect('accounts:signup')

    else:
      hashedpwd = make_password(password)
      user = User.objects.create(username= username , password = hashedpwd)
      user.save()
      messages.success(request, "Account Successfully Created ")
      return redirect('accounts:login')
      
 

      

  return render(request,'accounts/signup.html')



def LoginView(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username , password=password)
    
    if user is not None:
      login(request, user)
    else:
      None

    return redirect("gallery:create")

  return render(request,'accounts/login.html')


  
def logout_view(request):
  if request.method=="POST":
    logout(request)
    return redirect('gallery:homepage')
  
  
