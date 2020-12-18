from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Gallery(models.Model):
  title=models.CharField(max_length=50)
  slug=models.SlugField()
  thumb=models.ImageField(default='default.png',null=False)
  date=models.DateField(auto_now_add=True)
  author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
 
  
  
  def __str__(self):
    return self.title
  
  
