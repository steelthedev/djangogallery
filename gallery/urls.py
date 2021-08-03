from django.urls import path,include
from . import views

app_name='gallery'

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('create', views.Create , name="create")
   
]