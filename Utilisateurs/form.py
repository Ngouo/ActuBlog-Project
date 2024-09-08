from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProfileModel
from django import forms 


class SignUpForm(UserCreationForm):
  email = forms.EmailField()
  
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
   
   
  def __init__(self, *args, **kwargs):                          #cette fonction permet d'enlever toutes les ecritures qui sont sur les
     super(SignUpForm, self).__init__(*args, **kwargs)          #formulaires générés par Django
     
     for fieldname in  ['username', 'email', 'password1', 'password2']:
       self.fields[fieldname].help_text = None
       
       
       
       
class UserUpdateForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ["username", 'email']
    
    
  def __init__(self, *args, **kwargs):                          #cette fonction permet d'enlever toutes les ecritures qui sont sur les
     super(UserUpdateForm, self).__init__(*args, **kwargs)          #formulaires générés par Django
     
     for fieldname in  ['username', 'email',]:
       self.fields[fieldname].help_text = None
    
    
class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = ProfileModel
    fields = ['image']