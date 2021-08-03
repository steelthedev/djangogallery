from django.db import models
from django.contrib.auth.models import User
import string
import random
from django.utils.text import slugify
# Create your models here.



def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


class Gallery(models.Model):
  name=models.CharField(max_length=50)
  slug=models.SlugField()
  thumb=models.ImageField(blank=True ,null=True )
  date=models.DateField(auto_now_add=True)
  category = models.CharField(null=True , blank=True , max_length=200)
  author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
 
  
  def save(self, *args, **kwargs):
      if not self.slug:
        self.slug = slugify(rand_slug() + "-" + self.name)
        super(Gallery, self).save(*args, **kwargs)


  def __str__(self):
    return self.name
  
  
