from django.shortcuts import render,redirect
from .models import Gallery
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def homepage(request):

  gallery = Gallery.objects.all()

  context = {

    'gallery':gallery
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
        gallery = Gallery.objects.create(name=name, category = category , thumb = image  )
        gallery.save()
        return redirect("gallery:homepage")
      
  return render(request, 'gallery/gallerycreate.html')
  
