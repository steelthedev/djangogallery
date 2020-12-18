from django.urls import path,include
from . import views

app_name='gallery'

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('newsfeed/',views.newsfeed,name='newsfeed'),
    path('createshare/',views.createshare,name="create"),
    path('newsfeed/<slug:slug>',views.sharedetails,name="details"),
    
]