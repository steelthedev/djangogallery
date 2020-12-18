from . import models
from django import forms

class CreateShare(forms.ModelForm):
  class Meta:
    model=models.Gallery
    fields=['title','slug','thumb']
    widgets={
      'title':forms.TextInput(
        attrs={
       'class':'form-control'
      }),
      
      'slug':forms.TextInput(
        attrs={
       'class':'form-control'
      }),
      
      'thumb':forms.FileInput(
        attrs={
       'class':'form-control'
      }),
    }
  