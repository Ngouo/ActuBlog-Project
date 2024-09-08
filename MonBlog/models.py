from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PostModel(models.Model):
  title = models.CharField(max_length=150)
  contenu = models.TextField()
  auteur = models.ForeignKey(User ,on_delete=models.CASCADE, default=True)
  date_publication = models.DateTimeField(auto_now=True)
  
  
  
  class Meta:
    ordering = ('-date_publication', )
    
    
  def commentaire_count(self):
    return self.commentaire_set.all().count()
  
  
  def comments(self):
    return self.commentaire_set.all()

  def __str__(self):
      return self.title


class Commentaire(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
  contenu = models.CharField(max_length=200)
  
  def __str__(self):
    return self.contenu