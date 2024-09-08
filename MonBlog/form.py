from django import forms
from .models import PostModel, Commentaire


class PostModelForm(forms.ModelForm):
  contenu = forms.CharField(widget=forms.Textarea(attrs={'rows':8}))
  class Meta:
    model = PostModel
    fields = ('title', 'contenu')
    
    

class PostUpdateForm(forms.ModelForm):
  class Meta:
    model = PostModel
    fields = ['title', 'contenu']
    
    
    
class CommentForm(forms.ModelForm):
  contenu = forms.CharField(label='', 
                            widget= forms.TextInput(attrs={"placeholder":'Ajouter un commentaire...'}))
  
  class Meta:
    model = Commentaire
    fields =['contenu']
  