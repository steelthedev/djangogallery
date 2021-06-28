from django.urls import path
from . import views

app_name='accounts'

urlpatterns = [
    path('signup/',views.signup,name="signup"),
    path('login/',views.LoginView,name='login'),
    path('logout/',views.logout_view,name="logout"),
    
  ]