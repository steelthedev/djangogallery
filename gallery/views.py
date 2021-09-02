from django.shortcuts import render,redirect
from .models import Gallery
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def homepage(request):

  gallery = Gallery.objects.all()


  context = {

    'gallery':gallery,
  
  }

  return render(request,'gallery/index.html', context)


def Create(request):
  if request.user.is_authenticated:
    if request.method == "POST":
      name = request.POST['img-name']
      category = request.POST['category']
      thumb = request.FILES.getlist('image')
      description = request.POST['description']
      

      for image in thumb:
        g = Gallery.objects.create( name=name, category = category , thumb = image )
      return redirect('gallery:homepage') 
      
  return render(request, 'gallery/gallerycreate.html')



def Search(request):
  if request.method == "POST":
    submit_button = request.POST["submit_search"]
    search = request.POST.get("search")
    result = Gallery.objects.filter(name__contains = search)
    result_lenght = len(result)
    context = {
      'result':result,
      'l':result_lenght
    }
    return render(request, 'gallery/search.html', context)
      


  
