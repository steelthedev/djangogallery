from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def signup(request):
  if request.method=='POST':
    form=UserCreationForm(request.POST)
    if form.is_valid():
      user=form.save()
      login(request,user)
      return redirect('gallery:newsfeed')
      
  else:
    form=UserCreationForm()
  return render(request,'accounts/signup.html',{'form':form})



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

  return render(request,'gallery/index.html')


  
def logout_view(request):
  if request.method=="POST":
    logout(request)
    return redirect('gallery:homepage')
  
  
